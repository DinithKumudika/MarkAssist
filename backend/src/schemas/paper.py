from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Paper(BaseModel):
     id: str
     user:str
     description:str
     paper:str
     markingScheme:str
     status:str