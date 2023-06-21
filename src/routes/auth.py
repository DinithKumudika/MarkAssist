from fastapi import APIRouter, Request, HTTPException, status 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from models.user import User, UserLogin
from schemas.user import userEntity, usersEntity
from utils.authorization import authenticate_user

router = APIRouter()

@router.post("/login", response_description="login a user")
async def login(user: UserLogin):
     try:
          is_authenticated = await authenticate_user(user.email, user.password)
     except HTTPException:
          return {"message": "invalid credentials"}


@router.post("/register", response_description="Create new user")
async def register(request: Request, user: User):
     user = jsonable_encoder(user)
     new_user = request.app.mongodb["users"].insert_one(user)
     user = usersEntity(request.app.mongodb["users"].find_one({"_id": new_user.inserted_id}))
     
     if user:
          return JSONResponse({
               "status": status.HTTP_201_CREATED, 
               "user": user
          }) 
     raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, 
          detail="couldn't create new user"
     )


@router.get("/token", response_description="get OAuth2 Token")
async def get_token():
     pass