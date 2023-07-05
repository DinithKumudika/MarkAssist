from fastapi import Request
from bson.objectid import ObjectId

import cv2
from google.cloud import vision

import os

from schemas.answer import Answer, AnswerCreate
import helpers

def extract_answers(paper_no):
     try:
          images = helpers.get_images(os.path.join('../data/images/paper/', paper_no))
          save_path = os.path.join('../data/answers/', paper_no)
          os.mkdir(save_path)
          
          answers = []
          answer_count = 0
     
          for img_idx, image in enumerate(images):
               src_image = cv2.imread(image)
               screen_width = helpers.get_screen_width()
               screen_height = helpers.get_screen_height() 
               sized_image = helpers.resize(src_image, screen_height, screen_width)
               contours = helpers.detect_edges(sized_image)
               
               answers.append({
                    "img_no": img_idx + 1,
                    "questions": []
               })
          
               for i, contour in enumerate(contours):
                    # precision for approximation
                    epsilon = 0.01 * cv2.arcLength(contour, True)
                    approx = cv2.approxPolyDP(contour, epsilon, True)
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = w / h
               
                    if aspect_ratio > 1 and w > 50 and h > 20 and cv2.contourArea(contour) > 100:
                         if w > 700:
                              cropped_answer = sized_image[y:y+h, x:x+w]
                              questions_on_page = answers[img_idx]["questions"]
                              questions_on_page.append({
                                   "answer": cropped_answer
                              })
                              answer_count += 1
          for page in answers:
               questions = page["questions"]
               questions.reverse()
               for i, question in enumerate(questions):
                    cv2.imwrite(f"{save_path}/{page['img_no']}_{i+1}.jpg", question['answer'])
          return str(answer_count)
     except OSError:
          print("Error")
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
               "text": scanned_text
          })
          
     return answers

class AnswerModel():
     collection: str = "answers"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def save_answer(self, request: Request, answer: AnswerCreate):
          answer = self.get_collection(request).insert_one(answer.dict())
          
          if answer:
               return answer.inserted_id
     
     def get_by_id(self, request: Request, id: str)->Answer:
          answer = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if answer:
               answer["id"] = str(answer["_id"])
               return answer
     
     def get_by_student(self, request: Request, student_id: str)->list:
          answers = list(self.get_collection(request).find({"studentId": student_id}))
          for answer in answers:
               answer["id"] = str(answer["_id"]) 
          return answers
     
     def get_by_indexNo(self, request: Request, indexNo: str)->list:
          answers = list(self.get_collection(request).find({"userId": indexNo}))
          for answer in answers:
               answer["id"] = str(answer["_id"]) 
          return answers
     
     def get_by_subject_student(self, request: Request, indexNo: str, subjectId: str)->list:
          answers = list(self.get_collection(request).find({"userId": indexNo,"subjectId": subjectId}))
          for answer in answers:
               answer["id"] = str(answer["_id"]) 
          return answers
     
     def get_by_paper(self, request: Request, paper_id: str)->list:
          answers = list(self.get_collection(request).find({}))
          for answer in answers:
               answer["id"] = str(answer["_id"]) 
          return answers