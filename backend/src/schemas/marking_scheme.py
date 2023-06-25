from pydantic import BaseModel, Field
from typing import Optional

class MarkingScheme(BaseModel):
     id: str
     subjectCode:str
     subjectName:str
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
            "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
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
        
class MarkingSchemeUpdate(BaseModel):
     markingUrl:str
           
     class Config:
        schema_extra = {
        "example": {
            "markingUrl":"https://firebasestorage.googleapis.com/v0/b/papermarkin.appspot.com/o/",
            }
        }

     



