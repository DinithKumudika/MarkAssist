from fastapi import Depends, HTTPException, Request, status

from schemas.user import userEntity
from utils.hashing import Hasher

async def authenticate_user(request:Request, email: str, password: str):
     user = userEntity(request.app.mongodb["users"].find_one({"email": email}))
     if not user:
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     if not Hasher.verify_password(password, user.password):
          raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Invalid credentials")
     # create the token and return it
     return {"status": 200, "authenticated": True}

