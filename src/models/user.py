from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
     firstName: str
     lastName: str
     email: str
     password: str
     userType: str
     emailActive: bool
     isDeleted: bool
     
     class Config:
          schema_extra = {
               "example": {
                    "firstName": "Dinith",
                    "lastName": "Kumudika",
                    "email": "dinith1999@gmail.com",
                    "password": "$2a$10$8KkORxP4/YpPBarYGKd6VO6aohKYAaDQC/9ZYZImj0Yf71VHGfGEG",
                    "userType": "student",
                    "emailActive": False,
                    "isDeleted": False
               }
          }
          
class UpdateUser(BaseModel):
     pass