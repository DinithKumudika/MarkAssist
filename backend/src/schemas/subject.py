from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Subject(BaseModel):
    id: str
    # subjectStream:str
    subjectCode:str
    subjectName:str
    year:int
    teacherId:str
    semester:int
    academicYear:int
    assignmentMarks:int
    paperMarks:int
    editingTeacher:str
    nonEditingTeacher:str
    

    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            # "subjectStream":"SCS",
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "teacherId": "64873b4029eb156b34979ab0",
            "semester":2 ,
            "academicYear":2,
            "assignmentMarks":30,
            "paperMarks":70,
            "editingTeacher":"Saman",
            "nonEditingTeacher":"Chaminda",
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

class GroupedSubject(BaseModel):
    subjectCode:str
    subjects: List[Subject]
    
    

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
    assignmentMarks:int
    paperMarks:int
    editingTeacher:str
    nonEditingTeacher:str
    createdAt: Optional[datetime] = Field(default_factory=datetime.now)
    updatedAt: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
        "example": {
            # "subjectStream":"SCS",
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "teacherId": "64873b4029eb156b34979ab0",
            "semester":2 ,
            "academicYear":2,
            "assignmentMarks":30,
            "paperMarks":70,
            "editingTeacher":"Saman",
            "nonEditingTeacher":"Chaminda",
            "createdAt": "2023-06-27T10:00:00",
            "updatedAt": "2023-06-27T10:00:00"
            }
        }