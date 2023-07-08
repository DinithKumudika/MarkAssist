from fastapi import APIRouter, Request, Response, HTTPException, status, BackgroundTasks
from bson.json_util import dumps
from typing import Optional, List
from pydantic import EmailStr
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schemas.user import User
from models.user import UserModel

# from utils.mailer import send_mail
# from utils.send_email import send_email_background,send_email_async
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
     
# @router.post("/send-email")
# def schedule_mail(req: MailBody, tasks: BackgroundTasks):
#     data = req.dict()
#     tasks.add_task(send_mail, data)
#     return {"status": 200, "message": "email has been scheduled"}

# @router.get('/send-email/asynchronous')
# async def send_email_asynchronous(to:EmailStr,subject:str,body:Optional[str]=None):
#     await send_email_async(
#         to,
#         subject,
#         body
#     )
#     return 'Success'

# @router.get('/send-email/backgroundtasks')
# async def send_email_backgroundtasks(background_tasks: BackgroundTasks,to:EmailStr,subject:str,body:Optional[str]=None):
#     send_email_background(
#         background_tasks,
#         subject,
#         to,
#         body
#     )
#     return 'Success'

@router.post('/send-email/mailDemo')
def send_email_tasks(to: EmailStr, subject: str, body: Optional[str] = None):
    try:
        send_email(to, subject, body)
        return {'message': 'Email sent successfully.'}
    except Exception as e:
        return {'message': str(e)}
