from pydantic import BaseModel, Field
from fastapi import UploadFile,File
from typing import Optional, List
from datetime import datetime


class MarkPercentage(BaseModel):
     minimum: int
     maximum: int
     percentageOfMarks: int
     
     class Config:
          schema_extra = {
               "example": {
                    "minimum": 0,
                    "maximum": 30,
                    "percentageOfMarks": 30
               }
          }


class MarkingScheme(BaseModel):
     id: str
     subjectCode:str|None
     subjectName:str|None
     year:int
     subjectId:str
     markingUrl:str
     markConfig: List[MarkPercentage]

     class Config:
          schema_extra = {
               "example": {
                    "id": "64882f6c32d15c1d89f06cdf",
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
                    "markConfig": [
                              {
                                   "minimum": 0,
                                   "maximum": 30,
                                   "percentageOfMarks": 30
                              },
                              {
                                   "minimum": 30,
                                   "maximum": 70,
                                   "percentageOfMarks": 70
                              },
                              {
                                   "minimum": 70,
                                   "maximum": 100,
                                   "percentageOfMarks": 100
                              }          
                    ],
               }
          }
          
          
class MarkingSchemeCreate(BaseModel):
     subjectCode:str
     subjectName:str
     year:int
     subjectId:str
     markingUrl:str
     markConfig: List[MarkPercentage]
     isProceeded: bool
     createdAt: Optional[datetime] = Field(default_factory=datetime.now)
     updatedAt: Optional[datetime] = Field(default_factory=datetime.now)

     class Config:
          schema_extra = {
               "example": {
                    "subjectCode": "SCS2213",
                    "subjectName":"DSA",
                    "year": 2022,
                    "subjectId": "64873b4029eb156b34979ab0",
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
                    "markConfig": [
                              {
                                   "minimum": 0,
                                   "maximum": 30,
                                   "percentageOfMarks": 30
                              },
                              {
                                   "minimum": 30,
                                   "maximum": 70,
                                   "percentageOfMarks": 70
                              },
                              {
                                   "minimum": 70,
                                   "maximum": 100,
                                   "percentageOfMarks": 100
                              }          
                         ],
                    "isProceeded": False,
                    "createdAt": "2023-06-27T10:00:00",
                    "updatedAt": "2023-06-27T10:00:00"
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
     markingUrl: Optional[str|None] = None
     markConfig: Optional[List[MarkPercentage]|None] = None
     class Config:
          schema_extra = {
               "example": {
                    "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
               }
          }

     



