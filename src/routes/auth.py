from fastapi import APIRouter, Body, Request, Response, HTTPException, status 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from models.user import User, UserLogin, UserCreate
from schemas.user import userEntity, usersEntity
from utils.authorization import authenticate_user, generate_token
from utils.hashing import Hasher

router = APIRouter()

@router.post("/login", response_description="login a user")
async def login(request: Request, payload: UserLogin = Body()):
     try:
          is_authenticated = await authenticate_user(request, payload.email, payload.password)
          if is_authenticated:
               token = generate_token(payload.dict())
          return JSONResponse(
               {
                    "token": token, 
                    "token_type": "bearer"
               }, 
               status_code=status.HTTP_200_OK
          )
     except HTTPException:
          return JSONResponse(
               {"message": "invalid credentials"}, 
               status_code=status.HTTP_401_UNAUTHORIZED
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
     user = usersEntity(request.app.mongodb["users"].find_one({"_id": new_user.inserted_id}))
     
     if user:
          return JSONResponse(
               {"data": user}, 
               status_code= status.HTTP_201_CREATED
          ) 
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )


@router.get("/token", response_description="get OAuth2 Token")
async def get_token():
     pass