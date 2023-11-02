from fastapi import Request
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from typing import Optional, Dict, Union
from config.database import Database
from schemas.student_subject import StudentSubjectBase, StudentSubject,StudentSubjectCreate

class StudentSubjectModel():
     collection: str = "student_subject"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_student_subject(self, request: Request) -> list:
          student_subjects = list(self.get_collection(request).find())
          for student_subject in student_subjects:
               student_subject["id"] = str(student_subject["_id"])

          return student_subjects
     
     def by_id(self, request: Request, id: str) -> StudentSubject:
          student_subject = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if student_subject:
               student_subject["id"] = str(student_subject["_id"])
          return student_subject

     def by_index(self, request: Request, index: str) -> StudentSubject:
          student_subject = self.get_collection(request).find_one({"index": str(index)})
          if student_subject:
               student_subject["id"] = str(student_subject["_id"])
          return student_subject
     
     def add_new_student_subject(self, request: Request, student_subject: StudentSubjectCreate) -> StudentSubject:
          print("This is add_new_student_subject function",student_subject)
          new_student_subject = self.get_collection(request).insert_one(jsonable_encoder(student_subject))

          inserted_id = new_student_subject.inserted_id
          inserted_student_subject= self.get_collection(request).find_one({"_id": inserted_id})
          if inserted_student_subject:
               inserted_student_subject["id"] = str(inserted_student_subject["_id"])

               # print("This is id",str(inserted_id));   
               return inserted_student_subject
          return None
      
     def update(self, request: Request, filters: Dict[str, Union[str, ObjectId]], data)-> StudentSubject | bool:
          print("filters", filters)
          print("data", data)
          updated_student_subject = self.get_collection(request).find_one_and_update(
               filters, 
               {'$set': data},
               return_document=ReturnDocument.AFTER
          )
          
          print("updated studentSubject", updated_student_subject)
          if updated_student_subject:
               updated_student_subject["id"] = str(updated_student_subject["_id"])
               return updated_student_subject
          else:
               return False
          
     def get_semester_results(self, request: Request, userIndex: str, semester:int, academicYear:int) -> list:
          student_subject = self.by_index(request, userIndex)
          
          subjects_results = []
          
          if student_subject:
               for subject in student_subject['subject']:
                    if subject['semester'] == semester and subject['academicYear'] == academicYear:
                         subjects_results.append(subject)
                    else:
                         continue
          
          return subjects_results
     
