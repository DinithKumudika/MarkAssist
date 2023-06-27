from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from config.database import Database
from schemas.subject import Subject

class SubjectModel():
     collection: str = "subjects"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_subjects(self, request: Request) -> list:
          subjects = list(self.get_collection(request).find())
          for subject in subjects:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
          return subjects
     
     def subject_by_id(self, request: Request, id: str) -> Subject:
          subject = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if subject:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
               return subject
     
     def delete_subject(self, request: Request, id: str):
          subject = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})
     

     # get a list of year according to a given year
     def get_years_by_subjectCode(self, request: Request, subjectCode: str) -> list:
          years = self.get_collection(request).distinct("year", {"subjectCode": subjectCode})
          if years:
               sorted_years = sorted(years)
               return sorted_years
          return None

          
     
     def get_subject_teacher(self, request: Request, id: str) -> list:
          teacher_id = ObjectId(id)

          subjects = self.get_collection(request).aggregate([
               { "$match": { "teacherId": teacher_id } },
               { "$sort": { "createdDate": 1 } },
               {
                    "$group": {
                         "_id": "$teacherId",
                         "subjects": { "$push": "$$ROOT" }
                    }
               }
          ])

          # Convert ObjectId to string for compatibility with the existing code
          for subject in subjects:
               # print("This is subject",subject)
               subject["_id"] = str(subject["_id"])
               for sub in subject["subjects"]:
                    sub["id"] = str(sub["_id"])
                    sub["teacherId"] = str(sub["teacherId"])
          new_subjects = subject['subjects']
          # print("This is new_subjects",new_subjects)
          return new_subjects
