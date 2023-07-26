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
     accuracy: Optional[float] = None
     marks: Optional[float] = None
     
class AnswerCreate(BaseModel):
     paperNo: str
     subjectId: str
     userId: str
     questionNo: str
     text: str
     uploadUrl: str
     accuracy: Optional[float] = None
     marks: Optional[float] = None
     
class AnswerUpdate(BaseModel):
     userId: str
     questionNo: str
     accuracy:float

