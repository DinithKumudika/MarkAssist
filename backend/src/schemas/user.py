from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
     id: str
     firstName: str
     lastName: str
     email: EmailStr
     userType: str
     emailActive: bool
     isDeleted: bool
     title:str|None
     role:str|None
     
     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False,
                    "title": "Dr",
                    "role": "Lecturer"
               }
          }


class UserBase(BaseModel):
     firstName: str
     lastName: str
     email: EmailStr
     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com"
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
     password: str
     userType: str
     emailActive: bool
     isDeleted: bool
     title:str|None
     role:str|None
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "$2a$10$8KkORxP4/YpPBarYGKd6VO6aohKYAaDQC/9ZYZImj0Yf71VHGfGEG",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False,
                    "title": "",
                    "role": ""
               }
          }

class TeacherCreate(UserBase):
     password: str|None
     userType: str
     emailActive: bool
     isDeleted: bool
     title:str
     role:str
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "123456",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False,
                    "title": "Dr",
                    "role": "Lecturer"
                    
               }
          }

class UserUpdate(UserBase):
     firsName: Optional[str] = None
     lastName: Optional[str] = None
     email: Optional[EmailStr] = None