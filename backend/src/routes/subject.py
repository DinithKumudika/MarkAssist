from fastapi import APIRouter, Request, Response, HTTPException, status
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schemas.subject import Subject 
from models.subject import SubjectModel

router = APIRouter()
subject_model = SubjectModel()


@router.get('/', response_description="Get Subjects", response_model=List[Subject],status_code=status.HTTP_200_OK)
async def get_subjects(request: Request, limit: Optional[int] = None):
     subjects = subject_model.list_subjects(request)
     
     if subjects:
          return subjects 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no subjects found"
     )


@router.get('/{id}', response_description="Get a subject by id", response_model=Subject,status_code=status.HTTP_200_OK)
async def get_subject_by_id(request: Request ,id: str):
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