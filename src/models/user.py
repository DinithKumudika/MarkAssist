from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
     id: str
     firstName: str
     lastName: str
     email: EmailStr
     

class UserBase(BaseModel):
     firstName: str
     lastName: str
     email: EmailStr
     password: str
     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "$2a$10$8KkORxP4/YpPBarYGKd6VO6aohKYAaDQC/9ZYZImj0Yf71VHGfGEG"
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

class UserCreate(UserBase):
     userType: str
     emailActive: bool
     isDeleted: bool
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
     firsName: Optional[str]
     lastName: Optional[str]
     email: Optional[EmailStr]