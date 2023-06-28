from fastapi import Depends, HTTPException, Request, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError

from datetime import datetime, timedelta

from models.user import UserModel
from schemas.user import User
from schemas.token import TokenData
from config.config import settings

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_token(data:dict):
     # payload
     to_encode = data.copy()
     expire_at = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     # add expiring time to payload
     to_encode.update({"exp": expire_at})
     
     jwt_token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
     
     return jwt_token


def verify_token(token:str, credentials_exception) -> TokenData:
     try:
          payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
          
          id: str = payload.get("user_id")
          username: str = payload.get("username")
          user_role: str = payload.get("user_role")
          
          if id is None or username is None or user_role is None:
               raise credentials_exception
          
          token_data = TokenData(
                         user_id=id, 
                         username=username, 
                         user_role=user_role
                    )
     except JWTError:
          raise credentials_exception
     
     return token_data


async def get_current_user(request: Request, token: str = Depends(oauth2_scheme)):
     credentials_exception= HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED, 
          detail="Could not validate credentials",
          headers={"WWW-Authenticate": "Bearer"},
     )
     try:
          token_data = verify_token(token, credentials_exception)
     except JWTError:
          print("authorization error")
     
     user_model = UserModel()
     user = user_model.by_id(request, token_data.user_id)
     if user is None:
          raise credentials_exception
     return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
     if current_user['isDeleted']:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST, 
               detail="inactive user"
          )
     else:
          return current_user