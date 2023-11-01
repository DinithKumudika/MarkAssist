from fastapi import APIRouter, Request, Response, HTTPException, status, Depends, Body
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from schemas.user import User,UserCreate,TeacherCreate
from models.user import UserModel

from models.student_subject import StudentSubjectModel
from schemas.student_subject import StudentSubjectBase, StudentSubject,StudentSubjectUpdate, StudentSubjectCreate

router = APIRouter()
user_model = UserModel()
student_subject_model = StudentSubjectModel()


# get student semester wise results
@router.get("/{user_id}/result/{semester}/{academicYear}", response_description="get student's semester wise results", response_model=List[StudentSubjectBase], status_code=status.HTTP_200_OK)
async def get_by_id(request: Request, user_id: str, semester:int, academicYear:int):
    
     # get student index no using user id
     user = user_model.by_id(request, user_id)
    
     semester_subject_list = student_subject_model.get_semester_results(request, user["studentIndex"], semester, academicYear)
     if semester_subject_list:
          return semester_subject_list 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no details about semester {semester} of academic year {academicYear} of index no {user['studentIndex']} student"
     )
     
     
# get student grade class rank credits
@router.get("/{user_id}/grade", response_description="get student grade class rank credits", response_model=StudentSubject, status_code=status.HTTP_200_OK)
async def get_by_id(request: Request, user_id: str):
    
     # get student index no using user id
     user = user_model.by_id(request, user_id)
    
     student_subject = student_subject_model.by_index(request, user["studentIndex"])
     if student_subject:
          return student_subject 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no details with the index of {user['studentIndex']}"
     )
     

#calculate student gpa
@router.post("/gpa", response_description="calculate student gpa", status_code=status.HTTP_200_OK)
async def calculate_gpa(request: Request):

     student_subject = student_subject_model.calculateGPA(request)
     # print("\n\nThis is student_subject in endpoint",student_subject,"\n\n")
     # print("5")
     if student_subject:
          print("6")
          return JSONResponse({
               "detail": "answers saved",
               "data": student_subject
          }, 
          status_code=status.HTTP_201_CREATED)
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no details with"
     )    