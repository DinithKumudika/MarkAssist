from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Subject(BaseModel):
    id: str
    subjectCode:str
    subjectName:str
    year:int
    teacherId:str
    semester:int
    academicYear:int
    

    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "teacherId": "64873b4029eb156b34979ab0",
            "semester":2 ,
            "academicYear":2,
            }
        }
        
class SubjectYearsByCode(BaseModel):
    year:int

    class Config:
        schema_extra = {
        "example": {
            "year": 2022,
        }
    }

# Add a new class for the response model
class YearsListResponse(BaseModel):
    __root__: List[SubjectYearsByCode]
    

class SubjectCreate(BaseModel):
    
    subjectCode:str
    subjectName:str
    year:int
    teacherId:str
    semester:int
    academicYear:int
    createdAt: Optional[datetime] = Field(default_factory=datetime.now)
    updatedAt: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "teacherId": "64873b4029eb156b34979ab0",
            "semester":2 ,
            "academicYear":2,
            "createdAt": "2023-06-27T10:00:00",
            "updatedAt": "2023-06-27T10:00:00"
            }
        }