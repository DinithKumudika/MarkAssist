from fastapi import APIRouter, Body, Depends, Request, Response, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from models.user import UserModel
from schemas.user import User, UserCreate
from schemas.token import Token
from utils.auth import generate_token
from utils.hashing import Hasher

router = APIRouter()
user_model = UserModel()

# login user
@router.post("/token", response_description="get OAuth2 Token", response_model=Token)
async def login(request: Request, payload: OAuth2PasswordRequestForm = Depends()):
     user = user_model.by_email(request, payload.username)
     if not user:
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED, 
               detail= "Invalid credentials"
          )
     if not Hasher.verify_password(payload.password, user["password"]):
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED, 
               detail= "Invalid credentials"
          )
     
     token = generate_token({
               "user_id": user["id"], 
               "username": user["email"],
               "user_role": user["userType"]
          })
     
     return Token(access_token=token, token_type="bearer")

# register new user
@router.post("/register", response_description="Create new user", response_model=User)
async def register(request: Request, payload: UserCreate = Body()) -> User:
     print("Data:", payload.dict())
     user = user_model.by_email(request, payload.email)
     print("Hello")
     if user:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST, 
               detail="user already exists"
          )
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


@router.get('/logout', response_description="logout user")
async def logout():
     pass


@router.post('/validate-email')
async def validate_email(request: Request, payload: str):
     pass


@router.post('/accountVerification')
async def send_verification_email(to:str):
     print("Working 1")
     try:
          # send_email_verification_email(to)
          print("Working 2")
          return JSONResponse(
               {'status': 'email sent'}, 
               status_code=status.HTTP_200_OK
          )
     except:
          return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/verify-email/{token}', response_description="verify email")
async def verify_email(request: Request, token: str):
     pass