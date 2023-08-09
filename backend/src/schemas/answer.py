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
     accuracy: Optional[float] = 0.0
     keywordsaccuracy: Optional[float] = 0.0
     marks: Optional[float] = 0.0
     
     
class AnswerCreate(BaseModel):
     paperNo: str
     subjectId: str
     userId: str
     questionNo: str
     text: str
     uploadUrl: str
     accuracy: Optional[float] = 0.0
     keywordsaccuracy: Optional[float] = 0.0
     marks: Optional[float] = 0.0
     
class AnswerUpdate(BaseModel):
     userId: str
     questionNo: str
     accuracy:float

