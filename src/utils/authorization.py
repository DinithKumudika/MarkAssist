from fastapi import Depends, HTTPException, Request, status
from jose import JOSEError, jwt

from datetime import datetime, timedelta

from schemas.user import userEntity
from utils.hashing import Hasher
from config.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate_token(data:dict):
     to_encode = data.copy()
     expire_at = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     to_encode.update({"exp": expire_at})
     
     jwt_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
     
     return jwt_token


async def authenticate_user(request: Request, email: str, password: str):
     user = userEntity(request.app.mongodb["users"].find_one({"email": email}))
     if not user:
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     if not Hasher.verify_password(password, user["password"]):
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     # create the token and return it
     return True