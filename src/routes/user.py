from fastapi import APIRouter, Request, Response, HTTPException, status
from bson.json_util import dumps
from typing import Optional, List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schemas.user import User
from models.user import UserModel

router = APIRouter()
user_model = UserModel()


@router.get('/', response_description="Get users", response_model=List[User],status_code=status.HTTP_200_OK)
async def read_users(request: Request, limit: Optional[int] = None):
     users = user_model.list_users(request)
     
     if users:
          return users 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )


@router.get('/{id}', response_description="Get a user by id", response_model=User,status_code=status.HTTP_200_OK)
async def get_by_id(request: Request ,id: str):
     user = user_model.by_id(request, id)
     if user:
          return user
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a user by id of {id}"
     )


@router.delete('/{id}', response_description="delete a user",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(request: Request, id: str):
     user = user_model.delete(request, id)
     if user:
          return Response(status_code=status.HTTP_204_NO_CONTENT)
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail= f"no user with the id of {id}"
     )