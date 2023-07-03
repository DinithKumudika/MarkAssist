from fastapi import APIRouter, Request, Response, HTTPException, status, Depends, Body
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from schemas.user import User,UserCreate,TeacherCreate
from models.user import UserModel
from utils.hashing import Hasher


router = APIRouter()
user_model = UserModel()

@router.get('/teachers', response_description="Get all teachers",response_model=List[User], status_code= status.HTTP_200_OK)
async def get_all_teachers(request:Request):
    users = user_model.list_teachers(request)
     
    if users:
          return users 
    raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )
    
@router.post("/teachers/new", response_description="Create new teacher", response_model=User)
async def register(request: Request, payload: TeacherCreate = Body()) -> User:
     print("Data:",payload)
     user = user_model.by_email(request, payload.email)
     print("Hello")
     if user:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST, 
               detail="user already exists"
          )
     payload.password = "123456";  #hard code the value
     payload.password = Hasher.get_password_hash(payload.password)
     new_user_id = user_model.create_user(request,payload)
     user = user_model.by_id(request,new_user_id)
     
     if user:
          print(user)
          return user
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )