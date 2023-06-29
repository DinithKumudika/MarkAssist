from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
     id: str
     firstName: str
     lastName: str
     email: EmailStr
     studentIndex: int
     isDeleted: bool
     
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