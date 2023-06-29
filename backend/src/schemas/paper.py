from pydantic import BaseModel, EmailStr, Field
from fastapi import UploadFile,File
from typing import Optional
from datetime import datetime

class Paper(BaseModel):
     id: str
     year: int
     subjectId:str
     subjectCode:str
     subjectName:str
     paper:str
     paperUrl:str
     
     class Config:
          schema_extra = {
               "example": {
                    "id": "64882f6c32d15c1d89f06cdf",
                    "year": 2022,
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "subjectId": "64873b4029eb156b34979ab0",
                    "paper": "20002115",
                    "paperUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
                    }
               }
          
          
class PaperCreate(BaseModel):
     year: int
     subjectId:str
     subjectCode:str
     subjectName:str
     paper:str
     paperUrl:str
     createdAt: Optional[datetime] = Field(default_factory=datetime.now)
     updatedAt: Optional[datetime] = Field(default_factory=datetime.now)
     
     class Config:
          schema_extra = {
               "example": {
                    "year": 2022,
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "subjectId": "64873b4029eb156b34979ab0",
                    "paper": "20002115",
                    "paperUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
                    }
               }
          
          
class PaperForm(BaseModel):
     file: UploadFile = File(...),
     year: int
     subjectId:str

     class Config:
          schema_extra = {
               "example": {
                    "file": "add a file",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
                    }
               }
