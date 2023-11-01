import time
from fastapi import Request
from bson.objectid import ObjectId
from pymongo import ReturnDocument 
from typing import Dict,List, Union

class GradeModel():
    collection: str = "grades"
     
    def get_collection(self, request: Request):
        return request.app.db[self.collection]
    
    def list_grades(self, request: Request) -> list:
        gradeList = self.get_collection(request).find() 
        return gradeList
    
    def grade_and_gpv(self, request: Request, marks: str):
        grade_list = self.list_grades(request)
        print("GRade List::::",grade_list)
        for grade in grade_list['grades']:
            if marks >= grade['start'] and marks <= grade['end']:
                return {"grade":grade['grade'], "gpv":grade['gpv']}
        return {"grade":"F", "gpv":0.0}
    

    def crete(self,request: Request, grades: List[Dict[str,Union[int,str,float]]]):
        gradeList = self.get_collection(request).insert_many(grades)
        return gradeList.inserted_ids
      

