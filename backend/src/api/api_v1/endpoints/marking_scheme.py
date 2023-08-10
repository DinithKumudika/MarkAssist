from fastapi import APIRouter, HTTPException, status, Request,Depends,UploadFile, File,Form
from fastapi.params import Body
from fastapi.responses import JSONResponse
from typing import List, Dict
from bson.objectid import ObjectId
import httpx
import random

import cv2
import numpy as np
from google.cloud import vision

import cv2
import numpy as np
from google.cloud import vision

import os

from models.marking_scheme import MarkingSchemeModel
from schemas.marking_scheme import MarkingScheme, MarkingSchemeCreate, MarkPercentage
from schemas.marking import MarkingUpdate
from models.marking import MarkingModel
from models.subject import SubjectModel

from schemas.user import User
from schemas.marking import Marking, MarkingCreate
from utils.auth import get_current_active_user
from utils.firebase_storage import upload_file, upload_file2 
import helpers

router = APIRouter()
marking_scheme_model = MarkingSchemeModel()
subject_model = SubjectModel()
marking_model = MarkingModel()

@router.get("/", response_description="Get all marking schemes",response_model=List[MarkingScheme])
async def get_All(request: Request):
     # print("This is user",current_user)
     markings = marking_scheme_model.list_marking_schemes(request)
     if markings:
          return markings 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="No marking schemes to show"
     )
     
     
@router.post("/", response_description="upload a marking scheme", response_model = MarkingScheme, status_code= status.HTTP_201_CREATED)
async def add_marking(request: Request, files: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...) ):
     
     # get the subjectCode and subjectName using subjectId
     subject = subject_model.subject_by_id(request, subjectId)
     print(subject)
     if(subject):
          
          # check if there any current marking scheme for this subject
          # TODO:update this query also to fit with a general find query
          current_marking = marking_scheme_model.get_marking_scheme_by_year_subjectId(request, int(year), subject['id'])
          print("This is current_marking",current_marking)
          
          if current_marking:
               marking_scheme_model.delete_single(request, "subjectId", subjectId)
               marking_model.delete(request, "subjectId", subjectId)
          
          
          marking_url = await upload_file(files,files.filename)  # Assuming you have implemented the `upload_file` function
          
          defaultMarkConfig = [
               {
                    "minimum": 0,
                    "maximum": 30,
                    "percentageOfMarks": 30
               },
               {
                    "minimum": 31,
                    "maximum": 70,
                    "percentageOfMarks": 70
               },
               {
                    "minimum": 71,
                    "maximum": 100,
                    "percentageOfMarks": 100
               }          
          ]
          # Create a new MarkingScheme object with the provided data and file URL
          marking_scheme = MarkingSchemeCreate(
               subjectCode=subject['subjectCode'],
               subjectName=subject['subjectName'],
               year= int(year),
               subjectId=subjectId,
               markingUrl=marking_url,
               markConfig=defaultMarkConfig
          )
          
          new_marking_scheme = await marking_scheme_model.add_new_marking(request, marking_scheme)
          print("New marking scheme",new_marking_scheme)
          if new_marking_scheme:
               marking_id = new_marking_scheme['id']
               # save marking scheme from cloud storage to local storage
               async with httpx.AsyncClient() as client:
                    response = await client.get(marking_url)
                    response.raise_for_status()
                    save_path = f"./../data/marking_schemes/{marking_id}.pdf"
                    with open(save_path, "wb") as files:
                         files.write(response.content)
               try:
                    # convert marking scheme to images
                    dir_path = os.path.join('./../data/images/marking_scheme', marking_id)
                    os.mkdir(dir_path)
                    images = helpers.convert_to_images(save_path, dir_path)
                    answers = []
                    answer_count = 0
                    keywords_count = 0
                    
                    # identify answer areas and keyword areas of marking scheme
                    for img_idx,image in enumerate(images):
                         src_image = cv2.imread(image)
                         screen_width = helpers.get_screen_width()
                         screen_height = helpers.get_screen_height() 
                         sized_image = helpers.resize(src_image, screen_height, screen_width)
                         contours = helpers.detect_edges(sized_image)
                         answers.append({
                              "img_no": img_idx + 1,
                              "questions": []
                         })
                         
                         question = {}
                         
                         for i, contour in enumerate(contours):
                              # precision for approximation
                              epsilon = 0.01 * cv2.arcLength(contour, True)
                              approx = cv2.approxPolyDP(contour, epsilon, True)
                              x, y, w, h = cv2.boundingRect(approx)
                              aspect_ratio = w / h
                              
                              questions_on_page = answers[img_idx]["questions"]
                              
                              if(('keywords' in question) and ('answer' in question)):               
                                   questions_on_page.append(question)
                                   print("answers scanned:", len(answers))
                                   print(f"no of questions on page {img_idx + 1}:", len(questions_on_page))
                         
                                   question = {}
               
                              if aspect_ratio > 1 and w > 50 and h > 20 and cv2.contourArea(contour) > 100:
                                   if w > 700 and h > 100:
                                        cropped_answer = sized_image[y:y+h, x:x+w]
                                        question["answer"] = cropped_answer
                                        answer_count += 1
                                        
                                   elif w > 700 and h <= 100:
                                        cropped_keywords = sized_image[y:y+h, x:x+w]
                                        question["keywords"] = cropped_keywords
                                        keywords_count += 1
                                        
                    save_path = os.path.join("../data/markings", marking_id)
                    answer_path = os.path.join(save_path, "answers")
                    keyword_path = os.path.join(save_path, "keywords")
                    
                    os.mkdir(save_path)
                    os.mkdir(answer_path)
                    os.mkdir(keyword_path)
                    
                    for page in answers:
                         # print(page)
                         questions = page["questions"]
                         questions.reverse()
                         for i, question in enumerate(questions):
                              cv2.imwrite(f"{answer_path}/{page['img_no']}_{i+1}_answer.jpg", question['answer'])
                              cv2.imwrite(f"{keyword_path}/{page['img_no']}_{i+1}_keywords.jpg", question['keywords'])
                    answers = []
                    keywords = []
                    client = vision.ImageAnnotatorClient()
                    # answer_path = os.path.join(f'./../data/markings/{marking_id}', "answers")
                    # keyword_path = os.path.join(f'./../data/markings/{marking_id}', "keywords")
                    answer_images = helpers.get_images(answer_path)
                    keyword_images = helpers.get_images(keyword_path)
                    
                    for i, image in enumerate(answer_images):
                         scanned_text = helpers.read_text(client, image)
                         answers.append({
                              "question no": i+1, 
                              "text": scanned_text
                         })
                    
                    for i, image in enumerate(keyword_images):
                         scanned_text = helpers.read_text(client, image)
                         keywords_arr = scanned_text.split(',')
                         keywords.append({
                              "question no": i+1, 
                              "keywords": keywords_arr
                         })
                    
                    print("answers:", answers)
                    print("keywords:", keywords)
                         
                    urls = []
                    markings = []
                    
                    for i, image in enumerate(answer_images):
                         with open(image, "rb") as files:
                              upload = UploadFile(filename=image, file=files)
                              filename = f"Q_{i+1}"
                              file_url = await upload_file2(upload, "uploads/images/answers/marking_schemes", marking_id, filename)
                              urls.append(file_url)
                         question_no = answers[i]["question no"]
                         answer_text = answers[i]["text"]
                         print("keywords::",keywords)
                         print("keywords[i]",keywords[i])
                         print("question_no",question_no)
                         if keywords[i]["question no"] == question_no:
                              extracted_keywords = keywords[i]["keywords"]
                         
                         marking = MarkingCreate(
                              subjectId=new_marking_scheme["subjectId"],
                              questionNo=question_no,
                              subQuestionNo='',
                              partNo='',
                              noOfPoints='',
                              marks='',
                              keywordsMarks='',
                              text=answer_text,
                              keywords=extracted_keywords,
                              uploadUrl=file_url,
                              markingScheme=marking_id,
                              selected=False
                         )
                         
                         new_marking_id = marking_model.save_marking(request, marking)
                         markings.append(str(new_marking_id))
                         
                    return JSONResponse({
                              "marking_urls": urls,
                              "marking_ids": markings
                         }, 
                         status_code=status.HTTP_200_OK
                    )
               except OSError:
                    return {"error": OSError}
               

          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="No marking schemes to show"
          )
     else:
          # no subject
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Add subject First"
          )


@router.get("/questions", response_description="get questions of a marking scheme by marking scheme id or subject id", response_model= List[Marking])
async def get_marking_content(request: Request, sub: str = None, scheme: str = None):
     if(sub):
          marking_questions = marking_model.get_by_subject(request, sub)
     
     if(scheme):
          marking_questions = marking_model.get_by_marking_scheme(request, scheme)
     
     if marking_questions:     
          return marking_questions
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"there is no paper with given id"
     )

# @router.get("/{schemeId}/questions", response_description="get questions of a marking scheme by marking scheme id", response_model= List[Marking])
# async def get_marking_content(request: Request, schemeId: str):
#      marking_questions = marking_model.get_by_marking_scheme(request, schemeId)
#      print(schemeId)
#      if marking_questions:
#           return marking_questions
#      raise HTTPException(
#           status_code=status.HTTP_404_NOT_FOUND, 
#           detail=f"there is no paper with id of {schemeId}"
#      )          


@router.get("/download/{scheme_id}", response_description="Download marking scheme from cloud storage")
async def download_paper(request: Request, scheme_id : str):
     marking = marking_scheme_model.by_id(request, scheme_id)
     
     if marking:
          document_url = marking["markingUrl"]
     
          async with httpx.AsyncClient() as client:
               response = await client.get(document_url)
               response.raise_for_status()
               save_path = f"./../data/marking_schemes/{scheme_id}.pdf"
               with open(save_path, "wb") as file:
                    file.write(response.content)
          try:
               dir_path = os.path.join('./../data/images/marking_scheme', scheme_id)
               os.mkdir(dir_path)
               images = helpers.convert_to_images(save_path, dir_path)
               
               return JSONResponse({
                    "status": status.HTTP_200_OK, 
                    "paper_path": document_url,
                    "images_created": len(images)
               }) 
          except OSError:
               return {"error": OSError}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{scheme_id}"
     )


@router.put('/update/grading/{markingSchemeId}', response_description="update an marking config of a marking scheme", response_model=MarkingScheme)
async def update_mark_config(request: Request, markingSchemeId: str, payload = Body(...)):
     print("markingSchemeId:",markingSchemeId)
     print("payload:", payload)
     updated_scheme = marking_scheme_model.update(request, "_id", ObjectId(markingSchemeId), {"markConfig": payload})
     if updated_scheme:
          return updated_scheme
     raise HTTPException(
          status_code=status.HTTP_304_NOT_MODIFIED, 
          detail=f"error updating marking scheme"
     )
     
@router.put('/update/{subjectId}', response_description="Update an existing marking scheme questions")
async def update_marking(request: Request, subjectId: str, payload: List[MarkingUpdate] = Body()):
     print("SubjectID:",subjectId)
     updates = []
     data_available=False
     for data in payload:
          print("datassss:",data)
          if data is not None:
               data_available=True
               updates.append(
                    {
                         "filter": {"_id": ObjectId(data.id), "subjectId": subjectId}, 
                         "update": {
                              "$set": {
                                   "questionNo": data.questionNo, 
                                   "subQuestionNo": data.subQuestionNo,
                                   "partNo": data.partNo,
                                   "noOfPoints": data.noOfPoints,
                                   "marks": data.marks,
                                   "keywordsMarks": data.keywordsMarks,
                                   "selected": data.selected
                              }
                         }
                    }
               )
     if data_available:
          update_count = marking_model.update_multiple(request, updates)
          if update_count:
               # TODO: return updated answer entries
               print("update_count:",update_count)
               updated_scheme = marking_scheme_model.update(request, "subjectId", str(subjectId), {"isProceeded": True})
               return JSONResponse(
                    {
                         "detail": f"{update_count} answers updated"
                    }, 
                    status_code=status.HTTP_200_OK
               )
          raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
               detail="update failed"
          )
     

# get marking scheme by  subjectId
@router.get("/{subjectId}", response_description="Get a marking scheme subjectId", response_model = MarkingScheme)
async def get_by_subjectId_year(request:Request, subjectId:str):
     # insertedYear = int(year)
     subject_id = subjectId
     # print(insertedYear,subject_id)
     marking= marking_scheme_model.get_marking_scheme_by_subjectId(request,subject_id)
     print(marking)
     if marking:
          return marking
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of {subjectId}"
     )
