from fastapi import Depends, HTTPException, Request, status
from passlib.context import CryptContext

from schemas.user import userEntity

pwd_context = CryptContext(schemes=["brcypt"], deprecated="auto")

def verify_password(password: str, hashed_password: str) -> bool:
     return pwd_context.verify(secret=password, hash=hashed_password)


def get_password_hash(password: str) -> str:
     return pwd_context.hash(password)


async def authenticate_user(request:Request, email: str, password: str):
     user = userEntity(request.app.mongodb["users"].find_one({"email": email}))
     if not user:
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     if not verify_password(password, user.password):
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     # create the token and return it
     return {"status": 200, "authenticated": True}

