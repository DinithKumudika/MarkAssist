from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Paper(BaseModel):
     id: str
     user:str
     description:str
     paper:str
     markingScheme:str
     status:str
     # id: str
     # subject:id
     # user:str
     # file_name_orginal:str,
     # paper_url:str