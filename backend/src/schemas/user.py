from bson import ObjectId
from datetime import datetime
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

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Dinith",
                "lastName": "Kumudika",
                "email": "dinith1999@gmail.com",
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


class UserCreate(UserBase):
    emailActive: bool = False
    verificationCode: str = None
    isDeleted: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Dinith",
                "lastName": "Kumudika",
                "email": "dinith1999@gmail.com",
                "password": "$2a$10$8KkORxP4/YpPBarYGKd6VO6aohKYAaDQC/9ZYZImj0Yf71VHGfGEG",
                "userType": "student",
                "emailActive": False,
                "verificationCode": "",
                "isDeleted": False,
                "createdAt": "",
                "updatedAt": ""
            }
        }


class StudentCreate(UserCreate):
    password: str
    userType: str = "student"
    studentIndex: int

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Dinith",
                "lastName": "Walpitagama",
                "email": "dinithwalpitagama@gmail.com",
                "password": "Dinith@123",
                "userType": "student",
                "emailActive": False,
                "isDeleted": False,
                "studentIndex": 20020697,                
                "createdAt": "",
                "updatedAt": ""

            }
        }

# TODO: set a default password
class TeacherCreate(UserCreate):
    password: str | None = None
    userType: str = "teacher"
    title: str
    role: str

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Dinith",
                "lastName": "Kumudika",
                "email": "dinith1999@gmail.com",
                "password": "123456",
                "userType": "teacher",
                "emailActive": False,
                "isDeleted": False,
                "title": "Dr",
                "role": "Lecturer",                
                "createdAt": "",
                "updatedAt": ""

            }
        }


class UserUpdate(UserBase):
    firsName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[EmailStr] = None


class UserVerify(BaseModel):
    emailActive: bool = False
    verificationCode: str | None = None
    updatedAt: datetime | None = None

# class AddTecherPassword(BaseModel):
#     emailActive: bool = False
#     updatedAt: datetime | None = None
#     password: str
    
class AddTecherPassword(UserVerify):
    password: str
