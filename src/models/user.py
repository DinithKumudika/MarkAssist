from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
     firstName: str
     lastName: str
     email: EmailStr
     password: str
     userType: str
     emailActive: bool
     isDeleted: bool
     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "dinith@123",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False
               }
          }


class UserLogin(BaseModel):
     email: EmailStr
     password: str
     
     class Config:
          schema_extra = {
               "example": {
                    "email": "dinith1999@gmail.com",
                    "password": "Dinith@123"
               }
          }

class UserCreate(User):
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "$2a$10$8KkORxP4/YpPBarYGKd6VO6aohKYAaDQC/9ZYZImj0Yf71VHGfGEG",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False
               }
          }


class UserUpdate(BaseModel):
     pass

