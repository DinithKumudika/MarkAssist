from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Answer(BaseModel):
     id: str
     paperNo: str
     subjectId: str
     userId: str
     questionNo: str
     text: str
     uploadUrl: str
     
     
class AnswerCreate(BaseModel):
     paperNo: str
     subjectId: str
     userId: str
     questionNo: str
     text: str
     uploadUrl: str
     
class AnswerUpdate(BaseModel):
     pass

