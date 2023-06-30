from fastapi import APIRouter, Body, HTTPException, Request, Response, status, UploadFile, File,Form,Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
import httpx
import requests

import os

from models.paper import PaperModel
from schemas.paper import Paper,PaperCreate,PaperForm

from models.user import UserModel
from schemas.user import User

from models.subject import SubjectModel;

from utils.auth import get_current_active_user

from utils.firebase_storage import upload_file 
import helpers

router = APIRouter()
paper_model = PaperModel()
subject_model = SubjectModel()
user_model = UserModel()

@router.get("/", response_description="Get all papers", response_model=List[Paper])
async def get_all_papers(request: Request, current_user: User = Depends(get_current_active_user)):
     papers = paper_model.list_papers(request)
     if papers:
          return papers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="No papers to show"
     )


# get paper by id
@router.get("/{paper_id}", response_description="Get a paper by id", response_model=Paper)
async def get_by_id(request: Request, paper_id, current_user: User = Depends(get_current_active_user)):
     paper = paper_model.by_id(request, paper_id)
     if paper:
          return paper 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )


@router.get("/download/{paper_id}", response_description="Download paper from cloud storage")
async def download_paper(request: Request, paper_id: str):
     paper = paper_model.by_id(request, paper_id)
     
     if paper:
          document_url = paper["paperUrl"]
     
          async with httpx.AsyncClient() as client:
               response = await client.get(document_url)
               response.raise_for_status()
               save_path = f"./../data/papers/{paper_id}.pdf"
               with open(save_path, "wb") as file:
                    file.write(response.content)
          try:
               dir_path = os.path.join('./../data/images/paper', paper_id)
               os.mkdir(dir_path)
               images = helpers.convert_to_images(save_path, dir_path)
               
               return JSONResponse({
                         "paper_path": document_url,
                         "images_created": len(images)
                    },
                    status_code=status.HTTP_200_OK
               ) 
          except OSError:
               return {"error": OSError}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )


@router.get("/user/{user_id}", response_description="Get papers by user id",response_model=List[Paper])
async def get_paper_by_uid(request: Request, user_id):
     uid = ObjectId(user_id)
     # papers = papersEntity(request.app.mongodb["tickets"].find({"user": uid}))
     papers = paper_model.by_user_id(request,uid)
     if papers:
          return papers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"No papers related to user with id of {user_id}"
     )


# add pdf page images to cloud storage and save in database
@router.post("/{paper_id}/images")
async def create_images(request:Request, payload: dict = Body(...)):
     paper_no = payload["paperNo"]
     return JSONResponse({
          "status": status.HTTP_201_CREATED, 
          "paper no": paper_no
     }) 


@router.get("/{paper_id}/images")
async def create_images(request:Request, paper_id):
     # paper = await paperEntity(request.app.mongodb["tickets"].find_one({"_id": ObjectId(paper_id)}))
     paper_id =  ObjectId(paper_id)
     paper = await paper_model.by_id(request, paper_id)
     paper_path = paper["paper"]
     
# @router.post('/upload/file/')
# async def upload_files(request: Request, files: List[UploadFile] = File(...)):
#      for file in files:
#           paper_url = await upload_file(file, file.filename)
          
#           data = {
#                "status":200,
#                "message": "File uploaded successfully",
#                "paper_url":paper_url
#           }
          
#      return "File upload success";

@router.post('/upload/file/')
async def upload_files(request: Request, file: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...)):     
     # get the subjectCode and subjectName using subjectId
     subject = subject_model.subject_by_id(request, subjectId)
     if(subject):
          # print("There is subject")
          # print(subject['subjectName'])
          # print(subject['subjectCode'])
          # print(file.filename)

          # Upload the file and get the file URL
          paper_url_up = await upload_file(file,file.filename)
          print(paper_url_up)

          # Create a new paper object with the provided data and file URL
          paper = PaperCreate(
               year=year,
               subjectId=subjectId,
               subjectCode=subject['subjectCode'],
               subjectName=subject['subjectName'],
               paper = file.filename,
               paperUrl= paper_url_up,
          )
          # print(paper);

          # Save the paper to the database using your model
          new_paper = await paper_model.add_new_paper(request, paper)
          if new_paper:
               return JSONResponse({
                    "detail": "new paper added", 
                    "data": new_paper
                    }, 
                    status_code=status.HTTP_200_OK
               )

          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="error in file upload"
          )
     else:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Add subject First"
          )
     
