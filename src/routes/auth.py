from fastapi import APIRouter, Body, Depends, Request, Response, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schemas.user import User, UserLogin, UserCreate
from schemas.token import Token
from utils.auth import generate_token
from utils.hashing import Hasher

router = APIRouter()

@router.post("/login", response_description="login a user", response_model=Token)
async def login(request: Request, payload: OAuth2PasswordRequestForm = Depends()):
     user = userEntity(request.app.mongodb["users"].find_one({"email": payload.username}))
     if not user:
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN, 
               detail= "Invalid credentials"
          )
     if not Hasher.verify_password(payload.password, user["password"]):
          raise HTTPException(
               status_code=status.HTTP_403_FORBIDDEN, 
               detail= "Invalid credentials"
          )
     
     token = generate_token({
               "user_id": user["id"], 
               "username": user["email"]
          })
     
     return JSONResponse(
          {
               "token": token, 
               "token_type": "bearer"
          }, 
          status_code=status.HTTP_200_OK
     )


@router.post("/register", response_description="Create new user")
async def register(request: Request, payload: UserCreate = Body()):
     user = usersEntity(request.app.mongodb["users"].find_one({"email": UserCreate.email}))
     if user:
          return JSONResponse(
               {"message": "user already exists"}, 
               status_code=status.HTTP_200_OK
          )
          
     payload.password = Hasher.get_password_hash(payload.password)
     new_user = request.app.mongodb["users"].insert_one(payload)
     user = request.app.mongodb["users"].find_one({"_id": new_user.inserted_id})
     
     if user:
          return JSONResponse(
               {"user": user}, 
               status_code= status.HTTP_201_CREATED
          ) 
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )


@router.get("/token", response_description="get OAuth2 Token")
async def get_token():
     pass