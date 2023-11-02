import time
from fastapi import Request
from bson.objectid import ObjectId
from pymongo import ReturnDocument 
from typing import Dict,List, Union

class GradeModel():
    collection: str = "grades"
     
    def get_collection(self, request: Request):
        return request.app.db[self.collection]
    
    def list_grades(self, request: Request):
        gradeList = self.get_collection(request).find({"_id": ObjectId("6541049ecee01459b6ad7055")})
        grades = [grade for grade in gradeList]
        return grades

    
    def grade_and_gpv(self, request: Request, marks: str):
        grade_list = self.list_grades(request)
        print("GRade List::::", grade_list[0]['grades'])
        print("Marks::::", marks)
        for grade in grade_list[0]['grades']:
            if float(marks) >= grade['start'] and float(marks) <= grade['end']:
                return {"grade":grade['grade'], "gpv":grade['gpv']}
        return {"grade":"F", "gpv":0.0}
    

    def crete(self,request: Request, grades: List[Dict[str,Union[int,str,float]]]):
        gradeList = self.get_collection(request).insert_many(grades)
        return gradeList.inserted_ids
      

