from fastapi import APIRouter, Request, HTTPException, status 
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from models.user import User
from schemas.user import userEntity, usersEntity

router = APIRouter()


@router.get('/', response_description="Get users")
async def read_users(request: Request ,limit: Optional[int] = None):
     users = usersEntity(request.app.mongodb["users"].find())
     if users:
          return JSONResponse({
               "status": status.HTTP_200_OK, 
               "data": {
                    "users": users
               }
          })
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )


@router.get("/token", response_description="get OAuth2 Token")
async def get_token():
     pass


@router.get('/{id}', response_description="Get a user by id")
async def get_by_id(request: Request ,id: str):
     user = userEntity(request.app.mongodb["users"].find_one({"_id": ObjectId(id)}))
     if user:
          return JSONResponse({
               "status": status.HTTP_200_OK, 
               "user": user
          }) 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a user by id of {id}"
     )