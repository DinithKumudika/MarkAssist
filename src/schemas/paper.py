# def paperEntity(item) -> dict:
#      return {
#           "id": str(item["_id"]),
#           "user": str(item["user"]),
#           "description": item["description"],
#           "paper_path": item["paper"],
#           "marking_scheme_path": item["markingScheme"]
#      }

# def papersEntity(entity) -> list:
#      return [paperEntity(item) for item in entity]


from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Paper(BaseModel):
     id: str
     user:str
     description:str
     paper:str
     markingScheme:str
     status:str
     


     
     



