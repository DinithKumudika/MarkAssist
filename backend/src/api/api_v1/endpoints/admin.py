from fastapi import APIRouter, Request, Response, HTTPException, status, Depends, Body
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from schemas.subject import Subject, SubjectCreate
from models.subject import SubjectModel

from schemas.user import User,UserCreate,TeacherCreate
from models.user import UserModel
from utils.hashing import Hasher


router = APIRouter()
user_model = UserModel()
subject_model = SubjectModel()

@router.get('/teachers', response_description="Get all teachers",response_model=List[User], status_code= status.HTTP_200_OK)
async def get_all_teachers(request:Request):
    users = user_model.list_teachers(request)
     
    if users:
          return users 
    raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )
# get subjects list
@router.get('/subjects', response_description="Get all Subjects", response_model=List[Subject],status_code=status.HTTP_200_OK)
async def get_subjects(request: Request, limit: Optional[int] = None):

     subjects = subject_model.list_subjects_distinct_subjectCode(request)
     
     if subjects:
          # print('Called get_subjects function',subjects)
          return subjects 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no subjects found"
     )

# get student list
@router.get('/students', response_description="Get all students",response_model=List[User], status_code= status.HTTP_200_OK)
async def get_all_students(request:Request):
     users = user_model.list_students(request)
      
     if users:
            return users 
     raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="no students found"
      )      

# get courses list
@router.get('/courses', response_description="Get all courses",response_model=List[Subject], status_code= status.HTTP_200_OK)
async def get_all_courses(request:Request):
     courses = subject_model.list_subjects_distinct_subjectCode(request)
      
     if courses:
            return courses 
     raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="no courses found"
      )      


# @router.post("/teachers/new", response_description="Create new teacher", response_model=User)
# async def register(request: Request, payload: TeacherCreate = Body()) -> User:
#      print("Data:",payload)
#      user = user_model.by_email(request, payload.email)
#      print("Hello")
#      if user:
#           raise HTTPException(
#                status_code=status.HTTP_400_BAD_REQUEST, 
#                detail="user already exists"
#           )
#      payload.password = "123456";  #hard code the value
#      payload.password = Hasher.get_password_hash(payload.password)
#      new_user_id = user_model.create_user(request,payload)
#      user = user_model.by_id(request,new_user_id)
     
#      if user:
#           print(user)
#           return user
#      raise HTTPException(
#           status_code=status.HTTP_400_BAD_REQUEST, 
#           detail="couldn't create new user"
#      )


# Add a new subject
# @router.post('/', response_description="Add a new subject", response_model= Subject, status_code= status.HTTP_201_CREATED)
# async def add_a_subject(request:Request, payload: SubjectCreate = Body(...)):
#      # print(payload)
     
#      # check if subject is existing in db by, subjectCode and year
#      current_subject = subject_model.get_subject_by_year_subjectCode(request,int(payload.year), payload.subjectCode)
     
#      if current_subject:
#           # There is a subject
#           raise HTTPException(
#                status_code=status.HTTP_400_BAD_REQUEST,
#                detail= f"Subject is already there"
#           )
#      else:
#           # no existing subject, new subject can be added
          
          
#           subject = SubjectCreate(
#                subjectCode = payload.subjectCode,
#                subjectName = payload.subjectName,
#                year = int(payload.year),
#                teacherId = payload.teacherId,
#                semester = int(payload.semester) ,
#                academicYear = int(payload.academicYear),
#                assignmentMarks =int(payload.assignmentMarks),
#                paperMarks = int(payload.paperMarks),
#                editingTeacher = payload.editingTeacher,
#                nonEditingTeaacher =payload.nonEditingTeaacher,
#                createdAt =  datetime.now(),
#                updatedAt = datetime.now()
#           )
          
#           new_subject = await subject_model.add_new_subject(request, subject);
          
#           if new_subject:
#                # print("This is inserted subject",new_subject)
#                return new_subject;
#           raise HTTPException(
#                status_code=status.HTTP_400_BAD_REQUEST,
#                detail= f" failed to add a new subject"
#           )
               
