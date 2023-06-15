from pydantic import BaseModel

import cv2
import numpy as np
from google.cloud import vision

import os

import config.config
import helpers

class Answer(BaseModel):
     pass

def extract_answers(paper_no):
     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.settings.GOOGLE_APPLICATION_CREDENTIALS
     count = 0
     
     try:
          images = helpers.get_images(os.path.join('./../data/images/', paper_no))
          save_path = os.path.join('./../data/answers/', paper_no)
          os.mkdir(save_path)
     
          for img_idx, image in enumerate(images):
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
               count = count + 1
          return str(count)
     except OSError:
          return None

def read_answers(paper_no):
     answers = []
     client = vision.ImageAnnotatorClient()
     answer_path = os.path.join('./../data/answers/', paper_no)
     answer_images = helpers.get_images(answer_path)
     
     for i, image in enumerate(answer_images):
          scanned_text = helpers.read_text(client, image)
          answers.append({
               "question no": i+1, 
               "answer": scanned_text
          })
          
     return answers