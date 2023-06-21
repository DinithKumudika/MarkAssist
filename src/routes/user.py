from fastapi import APIRouter, Request, Response, HTTPException, status 
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from models.user import User
from schemas.user import userEntity, usersEntity

router = APIRouter()


@router.get('/', response_description="Get users")
async def read_users(request: Request, limit: Optional[int] = None):
     users = usersEntity(request.app.mongodb["users"].find())
     if users:
          return JSONResponse(
               {"users": users}, 
               status_code=status.HTTP_200_OK
          )
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )


@router.get('/{id}', response_description="Get a user by id")
async def get_by_id(request: Request ,id: str):
     user = userEntity(request.app.mongodb["users"].find_one({"_id": ObjectId(id)}))
     if user:
          return JSONResponse(
               {"user": user}, 
               status_code= status.HTTP_200_OK
          ) 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a user by id of {id}"
     )


@router.delete('/{id}', response_description="delete a user")
async def delete_user(request: Request, id: str):
     user = userEntity(request.app.mongodb["users"].find_one({"_id": ObjectId(id)}))
     if user:
          deleted_user = request.app.mongodb["users"].find_one_and_delete({"_id": ObjectId(id)})
          return Response(status_code=status.HTTP_204_NO_CONTENT)
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail= f"no user with the id of {id}"
     )