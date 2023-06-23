from fastapi import Depends, HTTPException, Request, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError

from datetime import datetime, timedelta

from schemas.token import TokenData
from config.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_token(data:dict):
     to_encode = data.copy()
     expire_at = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     to_encode.update({"exp": expire_at})
     
     jwt_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
     
     return jwt_token


def verify_token(token:str, credentials_exception):
     try:
          payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
          id:str = payload.get("user_id")
          username:str = payload.get("username")
          
          if id is None or username is None:
               raise credentials_exception
          
          token_data = TokenData(user_id=id, username=username)
     except JWTError:
          raise credentials_exception
     
     return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
     credentials_exception= HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED, 
          detail="Could not validate credentials",
          headers={"WWW-Authenticate": "Bearer"},
     )
     token_data = verify_token(token, credentials_exception)
     
     