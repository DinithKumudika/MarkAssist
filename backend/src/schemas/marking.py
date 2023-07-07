from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Marking(BaseModel):
     id: str
     subjectId: str
     questionNo: str
     subQuestionNo: str
     partNo: str
     noOfPoints: str
     marks: str
     text: str
     uploadUrl: str
     markingScheme: str
     selected: bool

     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "studentIndex": "20020597",
                    "isDeleted": False
               }
          }

class MarkingCreate(BaseModel):
     subjectId: str
     questionNo: str
     subQuestionNo: str
     partNo: str
     noOfPoints: str
     marks: str
     text: str
     uploadUrl: str
     markingScheme: str
     selected: bool