from fastapi import Request
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from typing import Optional
from config.database import Database
from schemas.subject import Subject, SubjectCreate
import itertools

class SubjectModel():
     collection: str = "subjects"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_subjects_by_user_id(self, request: Request,user_id:str) -> list:
          subjects = list(self.get_collection(request).find({'teacherId':user_id}))
          for subject in subjects:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
          return subjects
     
     
     # get subject by subjectCode and user id as a list
     # def list_subjects_by_user_id(self, request: Request, user_id: str) -> list:
     #      subjects = list(self.get_collection(request).find({'teacherId': user_id}))
     #      subjects.sort(key=lambda x: x['subjectCode'])  # Sort the subjects by subject code
     #      grouped_subjects = []
     #      for subject_code, group in itertools.groupby(subjects, key=lambda x: x['subjectCode']):
     #           subjects_list = list(group)
     #           for subject in subjects_list:
     #                subject["id"] = str(subject["_id"]) 
     #                subject["teacherId"] = str(subject["teacherId"])
     #           grouped_subjects.append({
     #                "subjectCode": subject_code,
     #                "subjects": subjects_list
     #           })
     #      return grouped_subjects

     def list_subjects_by_user_id_distinct_subjectCode(self, request: Request, user_id: str) -> list:
          subjects = self.get_collection(request).distinct("subjectCode", {"teacherId": user_id})
          distinct_subjects = []
          for subject in subjects:
               subject_data = self.get_collection(request).find_one({"teacherId": user_id, "subjectCode": subject})
               subject_data["id"] = str(subject_data["_id"])
               subject_data["teacherId"] = str(subject_data["teacherId"])
               distinct_subjects.append(subject_data)
          return distinct_subjects

     
     
     # get subject by subjectCode and user id as a list
     def get_subject_by_subjectCode_userId(self,request:Request,user_id:str, subjectCode:str) -> list:
          print("This is user id",user_id)
          print("This is subjectCode",subjectCode)
          subjects = list(self.get_collection(request).find({"teacherId": user_id, "subjectCode":subjectCode}).sort("year", -1))
          if subjects:               
               print("No subjects",subjects)
               for subject in subjects:
                    subject["id"] = str(subject["_id"]) 
                    # print("This is subject id", subjects["id"])
                    subject["teacherId"] = str(subject["teacherId"]) 
               return subjects
          else:
               print("There are no subjects")
               return None
     
     
     def subject_by_id(self, request: Request, id: str) -> Subject:
          subject = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if subject:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
               return subject
          
     # get subject by subjectId and UserId
     def get_subject_by_id_user_id(self, request: Request,user_id:str, id: str) -> Subject:
          subject = self.get_collection(request).find_one({"_id": ObjectId(id),'teacherId':user_id})
          if subject:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
               return subject
     
     def delete_subject(self, request: Request, id: str):
          subject = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})
          
     # get subject by subjectCode and year
     def get_subject_by_year_subjectCode(self,request:Request,year:int, subjectCode:str) -> Subject:
          subject = self.get_collection(request).find_one({"year": year, "subjectCode":subjectCode})
          if subject:
               subject["id"] = str(subject["_id"]) 
               subject["teacherId"] = str(subject["teacherId"]) 
               return subject
          else:
               return None;

          
     
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
     

     async def add_new_subject(self, request: Request, new_subject: SubjectCreate) -> Optional[Subject]:
          result = self.get_collection(request).insert_one(dict(new_subject))
          # print("This is result",result)
          if result.inserted_id:
               # print(result.inserted_id)
               inserted_subject = self.get_collection(request).find_one({"_id": result.inserted_id})
               if inserted_subject:
                    inserted_subject["id"] = str(inserted_subject["_id"])
                    inserted_subject["teacherId"] = str(inserted_subject["teacherId"])
                    return Subject(**inserted_subject)
          return None
