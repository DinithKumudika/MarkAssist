from fastapi import APIRouter, Request, HTTPException, status 
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from config.database import Database
from models.user import User
from schemas.user import userEntity, usersEntity

router = APIRouter()


@router.get('/', response_description="Get users")
async def get_all(request: Request ,limit: Optional[int] = None):
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


@router.post("/login", response_description="login a user")
async def login():
     pass


@router.post("/register", response_description="Create new user")
async def create_user(request: Request, user: User):
     user = jsonable_encoder(user)
     new_user = request.app.mongodb["users"].insert_one(user)
     user = usersEntity(request.app.mongodb["users"].find_one({"_id": new_user.inserted_id}))
     
     if user:
          return JSONResponse({
               "status": status.HTTP_200_OK, 
               "user": user
          }) 
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )


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