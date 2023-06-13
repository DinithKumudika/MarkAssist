from fastapi import APIRouter
from fastapi.params import Body
from bson.objectid import ObjectId

import cv2
import numpy as np
from google.cloud import vision

import os

from config import config
from config.database import Database
from models.answer import Answer
from schemas.answer import answerEntity, answersEntity
import helpers

database = Database()
db = database.connect()
users_collection = db["answer"]
router = APIRouter(prefix="/answers")

@router.get("/answer/{paper_no}")
async def answer_to_text(paper_no):
     images = helpers.get_images(os.path.join(config.settings.IMAGE_DIR, paper_no))
     save_path = os.path.join(config.settings.CROPPED_ANSWERS_DIR, paper_no)
     client = vision.ImageAnnotatorClient()
     
     for img_idx, image in enumerate(images):
          os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'../venv/service_account.json'
          src_image = cv2.imread(image)
          screen_width = helpers.get_screen_width()
          screen_height = helpers.get_screen_height() 
          sized_image = helpers.resize(src_image, screen_height, screen_width)
          
          contours = helpers.detect_edges(sized_image)
          answers = []
          
          for i, contour in enumerate(contours):
               # precision for approximation
               epsilon = 0.01 * cv2.arcLength(contour, True)
               approx = cv2.approxPolyDP(contour, epsilon, True)
                         
               x, y, w, h = cv2.boundingRect(approx)
               aspect_ratio = w / h
               
               if aspect_ratio > 1 and w > 50 and h > 20 and cv2.contourArea(contour) > 100:
                    if w > 700:
                         cropped_answer = sized_image[y:y+h, x:x+w]
                         answers.append(cropped_answer)
          
     for ans_idx, answer in enumerate(answers):
          helpers.save_image(answer, save_path, ans_idx, img_idx)
          
     answer_images = helpers.get_images(save_path)
     for i, image in enumerate(answer_images):
          scanned_text = helpers.read_text(client, image)
          answers_collection = db["answers"]
          
          answers_collection.insert_one({
               "paperNo": paper_no,
               "questionNo": i + 1,
               "text": scanned_text
          })
          
          answers = answersEntity(answers_collection.find({"paperNo": paper_no}))
          return {"answers": answers}
          