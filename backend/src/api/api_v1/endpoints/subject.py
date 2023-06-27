from fastapi import APIRouter, Request, Response, HTTPException, status, Depends
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId 

from schemas.user import User
from schemas.subject import Subject, SubjectYearsByCode 
from models.subject import SubjectModel
from utils.auth import get_current_active_user

router = APIRouter()
subject_model = SubjectModel()


@router.get('/', response_description="Get Subjects", response_model=List[Subject],status_code=status.HTTP_200_OK)
async def get_subjects(request: Request, limit: Optional[int] = None):
     print(request.headers)
     print("Hello")
     subjects = subject_model.list_subjects(request)
     
     if subjects:
          return subjects 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no subjects found"
     )


@router.get('/{id}', response_description="Get a subject by id", response_model=Subject,status_code=status.HTTP_200_OK)
async def get_subject_by_id(request: Request ,id: str, current_user: User = Depends(get_current_active_user)):
     subject = subject_model.subject_by_id(request, id)
     if subject:
          return subject
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a subject by id of {id}"
     )


@router.delete('/{id}', response_description="delete a subject",status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(request: Request, id: str):
     subject = subject_model.delete_subject(request, id)
     if subject:
          return Response(status_code=status.HTTP_204_NO_CONTENT)
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail= f"no subject with the id of {id}"
     )
     
# get years list according to a subject code in  ascending order.
@router.get('/years', response_description=" get list of years according to subjectCode",status_code=status.HTTP_200_OK,response_model=List[SubjectYearsByCode])
async def get_years_list(request:Request, subjectCode:str):
     subject_list = subject_model.get_years_by_subjectCode(request,subjectCode)
     if subject_list:
          return subject_list;
     raise HTTPException(
          status_code= status.HTTP_404_NOT_FOUND,
          detail= f"No years for subject code {subjectCode}"
     )
     
@router.get('/teacher/{id}', response_description="Get subjects by teacher id",response_model= List[Subject],status_code=status.HTTP_200_OK)
async def get_subjects_by_teacher_id(request: Request, id: str):
     subjects = subject_model.get_subject_teacher(request, id)
     # subjects = list(subjects)
     # print ("This is subjects",(subjects))
     if subjects:
          return subjects
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail= f"no subjects with the teacher id of {id}"
     )
     
# Add a new subject
@router.post('/createSubject', response_description="Add a new subject", response_model= Subject, status_code= status.HTTP_201_CREATED)
async def add_a_subject(request):
     pass