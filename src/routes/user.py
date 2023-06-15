from fastapi import APIRouter, Body, HTTPException, status
from typing import Optional
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from config.database import Database
from models.user import User
from schemas.user import userEntity, usersEntity

database = Database()
db = database.connect()
users_collection = db["users"]
router = APIRouter(prefix="/users")


@router.get('/', response_description="Get users")
async def get_all(limit: Optional[int] = None):
     users = usersEntity(users_collection.find())
     if users:
          return {
               "status": status.HTTP_200_OK, 
               "data": {
                    "count": limit, 
                    "users": users
               }
          }
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )


@router.post("/login", response_description="login a user")
async def login():
     pass


@router.post("/register", response_description="Create new user")
async def create_user(user: User = Body(...)):
     user = jsonable_encoder(user)
     new_user = users_collection.insert_one(user)
     user = usersEntity(users_collection.find_one({"_id": new_user.inserted_id}))
     
     if user:
          return {"status": status.HTTP_200_OK, "user": user}
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )


@router.get('/{id}', response_description="Get a user by id")
async def get_by_id(id: str):
     user = userEntity(users_collection.find_one({"_id": ObjectId(id)}))
     if user:
          return {"status": status.HTTP_200_OK, "user": user}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a user by id of {id}"
     )