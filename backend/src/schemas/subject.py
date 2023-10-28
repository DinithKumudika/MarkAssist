from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class finalAssignmentMarks(BaseModel):
    index:Optional[str]|None
    assignment_marks:Optional[str]|None
    

    # subjectStream:str
class Subject(BaseModel):
    id: str
    subjectCode:str
    subjectName:str
    year:int
    semester:int
    academicYear:int
    no_credits:int
    assignmentMarks:int
    paperMarks:int
    editingTeacher:str
    nonEditingTeacher:str
    backgroundImage: int = 1
    finalAssignmentMarks: Optional[List[finalAssignmentMarks]] |None 
    
    
            # "subjectStream":"SCS",

    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "semester":2 ,
            "academicYear":2,
            "no_credits":2,
            "assignmentMarks":30,
            "paperMarks":70,
            "editingTeacher":"64873b4029eb156b34979ab0",
            "nonEditingTeacher":"64873b4029eb156b34979ab0",
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
    semester:int
    academicYear:int
    no_credits:int
    assignmentMarks:int
    paperMarks:int
    editingTeacher:str
    nonEditingTeacher:str
    backgroundImage: int = 1 
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    finalAssignmentMarks: Optional[List[finalAssignmentMarks]] |None 

            # "subjectStream":"SCS",
    class Config:
        schema_extra = {
        "example": {
            "subjectCode": "SCS2213",
            "subjectName":"DSA",
            "year": 2022,
            "semester":2 ,
            "academicYear":2,
            "no_credits":2,
            "assignmentMarks":30,
            "paperMarks":70,
            "editingTeacher":"64873b4029eb156b34979ab0",
            "nonEditingTeacher":"64873b4029eb156b34979ab0",
            "createdAt": "2023-06-27T10:00:00",
            "updatedAt": "2023-06-27T10:00:00"
            }
        }