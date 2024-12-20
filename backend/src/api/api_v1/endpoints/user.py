from fastapi import APIRouter, Request, Response, HTTPException, status, BackgroundTasks
from fastapi.responses import HTMLResponse
from bson.json_util import dumps
from typing import Optional, List
from pydantic import EmailStr
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schemas.user import User
from models.user import UserModel

from utils.emailer import send_email


router = APIRouter()
user_model = UserModel()


@router.get('/', response_description="Get users", response_model=List[User])
async def read_users(request: Request, limit: Optional[int] = None):
     users = user_model.list_users(request)
     
     if users:
          return users 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="no users found"
     )


@router.get('/{id}', response_description="Get a user by id", response_model=User)
async def get_by_id(request: Request , id: str):
     user = user_model.by_id(request, id)
     if user:
          return user
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"couldn't find a user by id of {id}"
     )


@router.delete('/{id}', response_description="delete a user")
async def delete_user(request: Request, id: str):
     user = user_model.delete(request, id)
     if user:
          return Response(status_code=status.HTTP_204_NO_CONTENT)
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail= f"no user with the id of {id}"
     )
     

@router.get('/send-email/mailDemo', response_class=HTMLResponse)
async def send_email_tasks(to: EmailStr, subject: str, name: str, verification_url: str,task:str=None):
     try:
          task = 'Email Verification'
          if task == 'Email Verification':        
               template_name = 'auth/send_email_verification_email.html'
               template_variables = {
                    'name': name,
                    'verification_url': verification_url
               }
               send_email(to, subject, template_name, template_variables)
               return "<h1>Email sent successfully.</h1>"
     except Exception as e:
          return str(e)
