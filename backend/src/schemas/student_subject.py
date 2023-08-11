from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class StudentSubjectBase(BaseModel):
    subject_id:str
    subject_code:str
    no_of_credit:int
    assignment_marks:float
    ocr_marks:float
    non_ocr_marks:float
    total_marks:float
    
    class Config:
        schema_extra = {
        "example": {
            "subject_id": "64882f6c32d15c1d89f06cdf",
            "subject_code": "SCS2213",
            "no_of_credit":3,
            "assignment_marks":30,
            "ocr_marks": 60,
            "non_ocr_marks":22 ,
            "total_marks":82,
            }
        }
    
class StudentSubject(BaseModel):
    id: str
    index:str
    gpa:float
    rank:int
    total_credit:float
    subject:List[StudentSubjectBase]
    
    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            "index": "20002114",
            "gpa":3.268,
            "rank": 104,
            "total_credit":2,
            "subject": [
                        {
                            "subject_id": "64882f6c32d15c1d89f06cdf",
                            "subject_code": "SCS2213",
                            "no_of_credit":3,
                            "assignment_marks":30,
                            "ocr_marks": 60,
                            "non_ocr_marks":22 ,
                            "total_marks":82,
                        },
                        {
                            "subject_id": "64882f6c32d15c1d89f06cdf",
                            "subject_code": "SCS2213",
                            "no_of_credit":3,
                            "assignment_marks":30,
                            "ocr_marks": 60,
                            "non_ocr_marks":22 ,
                            "total_marks":82,
                        },
                        {
                            "subject_id": "64882f6c32d15c1d89f06cdf",
                            "subject_code": "SCS2213",
                            "no_of_credit":3,
                            "assignment_marks":30,
                            "ocr_marks": 60,
                            "non_ocr_marks":22 ,
                            "total_marks":82,
                        }          
                ],
            }
        }
        
class StudentSubjectCreate(BaseModel):

    index:str
    gpa:float
    rank:int
    total_credit:float
    subject:List[StudentSubjectBase]
    
    class Config:
        schema_extra = {
        "example": {
            "id": "64882f6c32d15c1d89f06cdf",
            "index": "20002114",
            "gpa":3.268,
            "rank": 104,
            "total_credit":2,
            "subject": [
                        {
                            "subject_id": "64882f6c32d15c1d89f06cdf",
                            "subject_code": "SCS2213",
                            "no_of_credit":3,
                            "assignment_marks":30,
                            "ocr_marks": 60,
                            "non_ocr_marks":22 ,
                            "total_marks":82,
                        },         
                ],
            }
        }
        
        
class StudentSubjectUpdate(BaseModel):
    subject:List[StudentSubjectBase]
    
    class Config:
        schema_extra = {
        "example": {
            "subject": [
                        {
                            "subject_id": "64882f6c32d15c1d89f06cdf",
                            "subject_code": "SCS2213",
                            "no_of_credit":3,
                            "assignment_marks":30,
                            "ocr_marks": 60,
                            "non_ocr_marks":22 ,
                            "total_marks":82,
                        },
          
                ],
            }
        }
