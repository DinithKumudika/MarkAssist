from pydantic import BaseModel, Field
from fastapi import UploadFile,File
from typing import Optional

class MarkingScheme(BaseModel):
     id: str
     subjectCode:str|None
     subjectName:str|None
     year:int
     subjectId:str
     markingUrl:str

     class Config:
          schema_extra = {
               "example": {
                    "id": "64882f6c32d15c1d89f06cdf",
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/"
               }
          }
          
          
class MarkingSchemeCreate(BaseModel):
     subjectCode:str
     subjectName:str
     year:int
     subjectId:str
     markingUrl:str

     class Config:
          schema_extra = {
               "example": {
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
               }
          }

class MarkingSchemeForm(BaseModel):
     file: UploadFile = File(...)
     year:int
     subjectId:str

     class Config:
          schema_extra = {
               "example": {
                    "file":"Upload a file",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
               }
          }

class MarkingSchemeUpdate(BaseModel):
     markingUrl:str
     
     class Config:
          schema_extra = {
               "example": {
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
               }
          }

     



