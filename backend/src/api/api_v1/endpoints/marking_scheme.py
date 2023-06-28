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

import os

from models.marking_scheme import MarkingSchemeModel
from schemas.marking_scheme import MarkingScheme,MarkingSchemeCreate,MarkingSchemeForm

from models.subject import SubjectModel;

from schemas.user import User
from utils.auth import get_current_active_user
from utils.firebase_storage import upload_file 
import helpers

router = APIRouter()
marking_scheme_model = MarkingSchemeModel()
subject_model = SubjectModel()

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
     
@router.post("/", response_description="Add a marking scheme",response_model = MarkingScheme, status_code= status.HTTP_201_CREATED)
async def add_marking(request: Request, file: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...) ):
     # get the subjectCode and subjectName using subjectId
     subject = subject_model.subject_by_id(request, subjectId);
     if(subject):
          print("There is subject")
          # print(subject['subjectName'])
          # print(subject['subjectCode'])
          # print(file.filename)

          # Upload the file and get the file URL
          marking_url = await upload_file(file,file.filename)  # Assuming you have implemented the `upload_file` function

          # Create a new MarkingScheme object with the provided data and file URL
          marking_scheme = MarkingSchemeCreate(
               subjectCode=subject['subjectCode'],
               subjectName=subject['subjectName'],
               year=year,
               subjectId=subjectId,
               markingUrl=marking_url,
          )
          # print(marking_scheme);

          # Save the marking scheme to the database using your model
          new_marking_scheme = await marking_scheme_model.add_new_marking(request, marking_scheme)
          if new_marking_scheme:
               return new_marking_scheme

          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="No marking schemes to show"
          )
     else:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Add subject First"
          )

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
     
     
@router.put('/update', response_description="Update an existing marking scheme")
async def update_marking(request:Request,file: UploadFile = File(...),subjectCode: str = Form(...),year: int = Form(...),subjectId: str = Form(...)):
     pass


# @router.get("/{marking_id}", response_description="Get a marking scheme id")
# async def get_by_id(marking_id):
#      pass