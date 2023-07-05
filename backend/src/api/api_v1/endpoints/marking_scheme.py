from fastapi import APIRouter, HTTPException, status, Request,Depends,UploadFile, File,Form
from fastapi.params import Body
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter, HTTPException, status, Request,Depends,UploadFile, File,Form
from fastapi.params import Body
from fastapi.responses import JSONResponse
from typing import List
from bson.objectid import ObjectId
import httpx
from datetime import datetime

import cv2
import numpy as np
from google.cloud import vision

import os

from models.marking_scheme import MarkingSchemeModel
from schemas.marking_scheme import MarkingScheme,MarkingSchemeCreate,MarkingSchemeForm
from models.marking import MarkingModel
from models.subject import SubjectModel;

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
async def add_marking(request: Request, file: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...) ):
     
     # get the subjectCode and subjectName using subjectId
     subject = subject_model.subject_by_id(request, subjectId)
     print(subject)
     if(subject):
          
          # check if there any current marking scheme for this subject
          # TODO:update this query also to fit with a general find query
          current_marking = marking_scheme_model.get_marking_scheme_by_year_subjectId(request, int(year), subject['id'])
          print("This is current_marking",current_marking)
          
          if current_marking:
               #TODO:change update  
               marking_scheme_model.delete_by_subject(request, subjectId)
               marking_model.delete(request, "subjectId", subjectId)
          
          
          marking_url = await upload_file(file,file.filename)  # Assuming you have implemented the `upload_file` function
          
          # Create a new MarkingScheme object with the provided data and file URL
          marking_scheme = MarkingSchemeCreate(
               subjectCode=subject['subjectCode'],
               subjectName=subject['subjectName'],
               year= int(year),
               subjectId=subjectId,
               markingUrl=marking_url,
          )
          
          new_marking_scheme = await marking_scheme_model.add_new_marking(request, marking_scheme)
          if new_marking_scheme:
               marking_id = new_marking_scheme['id']
               # save marking scheme from cloud storage to local storage
               async with httpx.AsyncClient() as client:
                    response = await client.get(marking_url)
                    response.raise_for_status()
                    save_path = f"./../data/marking_schemes/{marking_id}.pdf"
                    with open(save_path, "wb") as file:
                         file.write(response.content)
               try:
                    # convert marking scheme to images
                    dir_path = os.path.join('./../data/images/marking_scheme', marking_id)
                    os.mkdir(dir_path)
                    images = helpers.convert_to_images(save_path, dir_path)
                    answers = []
                    answer_count = 0
                    # identify answer areas of marking scheme
                    
                    # identify answer areas of marking scheme
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
                    save_path = os.path.join("../data/markings", marking_id)
                    os.mkdir(save_path)
                    for page in answers:
                         # print(page)
                         questions = page["questions"]
                         # print(questions)
                         questions.reverse()
                         for i, question in enumerate(questions):
                              cv2.imwrite(f"{save_path}/{page['img_no']}_{i+1}.jpg", question['answer'])
                    
                    answers = []
                    client = vision.ImageAnnotatorClient()
                    answer_path = os.path.join('./../data/markings/', marking_id)
                    answer_images = helpers.get_images(answer_path)
                    for i, image in enumerate(answer_images):
                         scanned_text = helpers.read_text(client, image)
                         answers.append({
                              "question no": i+1, 
                              "text": scanned_text
                         })
                         
                    urls = []
                    markings = []
                    
                    for i, image in enumerate(answer_images):
                         with open(image, "rb") as file:
                              upload = UploadFile(filename=image, file=file)
                              filename = f"Q_{i+1}"
                              file_url = await upload_file2(upload, "uploads/images/answers/marking_schemes", marking_id, filename)
                              urls.append(file_url)
                         question_no = answers[i]["question no"]
                         answer_text = answers[i]["text"]
                         
                         marking = MarkingCreate(
                              subjectId=new_marking_scheme["subjectId"],
                              questionNo=question_no,
                              subQuestionNo='',
                              partNo='',
                              noOfPoints='',
                              marks='',
                              text=answer_text,
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
     
     
@router.put('/update/{subjectId}', response_description="Update an existing marking scheme questions")
async def update_marking(request: Request, subjectId: str, payload: Body()):
     updates = []
     for data in payload:
          updates.append(
               {
                    "filter": {"_id": ObjectId(data["id"]), "subjectId": subjectId}, 
                    "update": {
                         "$set": {
                              "questionNo": data["questionNo"], 
                              "subQuestionNo": data["subQuestionNo"],
                              "partNo": data["partNo"],
                              "noOfPoints": data["noOfPoints"],
                              "marks": data["marks"],
                              "selected": data["selected"]
                         }
                    }
               }
          )
     update_count = marking_model.update_multiple(request, updates)
     
     if update_count:
          # TODO: return updated answer entries
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
@router.get("/{year}/{subjectId}", response_description="Get a marking scheme subjectId and year", response_model = MarkingScheme)
async def get_by_subjectId_year(request:Request, year:int, subjectId:str):
     insertedYear = int(year)
     subject_id = subjectId
     print(insertedYear,subject_id)
     marking= marking_scheme_model.get_marking_scheme_by_year_subjectId(request,insertedYear,subject_id)
     print(marking)
     if marking:
          return marking
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of {subjectId}"
     )
