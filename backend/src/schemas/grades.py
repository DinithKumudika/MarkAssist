from pydantic import BaseModel, Field
from typing import Optional,List

class Grades(BaseModel):
     start: int
     end: int
     grade: str
     gpv: float

     
class GradesCreate(BaseModel):
    Grades:List[Grades]
     



