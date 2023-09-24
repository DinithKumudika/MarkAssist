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
     
     # get all subjects as a list
     def list_subjects(self, request: Request) -> list:
          subjects = list(self.get_collection(request).find())
          for subject in subjects:
               subject["id"] = str(subject["_id"])
               subject["editingTeacher"] = str(subject["editingTeacher"])
               subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
          return subjects
     
     
     # get a list of subjects by user id (editing or non editing)
     def list_subjects_by_user_id(self, request: Request, user_id: str) -> list:
          subjects = list(self.get_collection(request).find({
               "$or": [
                    {"editingTeacher": user_id},
                    {"nonEditingTeacher": user_id}
               ]
          }))

          for subject in subjects:
               subject["id"] = str(subject["_id"])
               subject["editingTeacher"] = str(subject["editingTeacher"])
               subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
          return subjects

     
     
     # get subject by subjectCode and user id as a list
     # def list_subjects_by_user_id(self, request: Request, user_id: str) -> list:
     #      subjects = list(self.get_collection(request).find({
     #           '$or':[
     #                {"editingTeacher":user_id},
     #                {"nonEditingTeacher":user_id}
     #           ]
     #      }))
     #      subjects.sort(key=lambda x: x['subjectCode'])  # Sort the subjects by subject code
     #      grouped_subjects = []
     #      for subject_code, group in itertools.groupby(subjects, key=lambda x: x['subjectCode']):
     #           subjects_list = list(group)
     #           for subject in subjects_list:
     #                subject["id"] = str(subject["_id"])
     #                subject["editingTeacher"] = str(subject["editingTeacher"])
     #                subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
     #           grouped_subjects.append({
     #                "subjectCode": subject_code,
     #                "subjects": subjects_list
     #           })
     #      return grouped_subjects
     
     
     
     # get the count of editing/nonEditing teachers distinctly
     # eg: teacherType = editingTeacher then it will return the count of editing teachers distinctly
     def count_teachers_distinct_teacher_type(self, request: Request, teacherType:str) -> list:
          teacherIds = self.get_collection(request).distinct(teacherType)
          return len(teacherIds)

     
     # get all subject as a list distinctly
     def list_subjects_distinct_subjectCode(self, request: Request) -> list:
          # in here we will only get the subject codes of the subjects as a list
          subjects = self.get_collection(request).distinct("subjectCode")
          distinct_subjects = []
          for subject in subjects:
               subject_data = self.get_collection(request).find_one({"subjectCode": subject})
               subject_data["id"] = str(subject_data["_id"])
               subject_data["editingTeacher"] = str(subject_data["editingTeacher"])
               subject_data["nonEditingTeacher"] = str(subject_data["nonEditingTeacher"])
               distinct_subjects.append(subject_data)
          return distinct_subjects
     
     def list_subjects_by_user_id_distinct_subjectCode(self, request: Request, user_id: str) -> list:
          subjects = self.get_collection(request).distinct("subjectCode", {
               "$or": [
                    {"editingTeacher": user_id},
                    {"nonEditingTeacher": user_id}
               ]
          })

          distinct_subjects = []
          for subject in subjects:
               subject_data = self.get_collection(request).find_one({
                    "$or": [
                         {"editingTeacher": user_id, "subjectCode": subject},
                         {"nonEditingTeacher": user_id, "subjectCode": subject}
                    ]
               })
               if subject_data:
                    subject_data["id"] = str(subject_data["_id"])
                    subject_data["editingTeacher"] = str(subject_data["editingTeacher"])
                    subject_data["nonEditingTeacher"] = str(subject_data["nonEditingTeacher"])
                    distinct_subjects.append(subject_data)

          return distinct_subjects

# get edinting and non edinting subjects by user id, if edinting is true, get editing subjects, else get non editing subjects
     def list_editing_subjects_by_user_id_distinct_subjectCode(self, request: Request, user_id: str, editing:bool ) -> list:
          
          subject = []
          subject_data = []
          
          # if editing is true, get editing subjects, else get non editing subjects
          if editing:
               subjects = self.get_collection(request).distinct("subjectCode", {"editingTeacher": user_id })
          else:
               subjects = self.get_collection(request).distinct("subjectCode", {"nonEditingTeacher": user_id }) 

          distinct_subjects = []
          for subject in subjects:
               
               if editing:
                    subject_data = self.get_collection(request).find_one({"editingTeacher": user_id, "subjectCode": subject})
               else:
                    subject_data = self.get_collection(request).find_one({"nonEditingTeacher": user_id, "subjectCode": subject})
                    
               if subject_data:
                    subject_data["id"] = str(subject_data["_id"])
                    subject_data["editingTeacher"] = str(subject_data["editingTeacher"])
                    subject_data["nonEditingTeacher"] = str(subject_data["nonEditingTeacher"])
                    distinct_subjects.append(subject_data)

          return distinct_subjects


     
     # get subject by subjectCode and user id as a list
     def get_subject_by_subjectCode_userId(self, request: Request, user_id: str, subjectCode: str) -> list:
          print("This is user id", user_id)
          print("This is subjectCode", subjectCode)
          
          subjects = list(self.get_collection(request).find({
               "$or": [
                    {"editingTeacher": user_id, "subjectCode": subjectCode},
                    {"nonEditingTeacher": user_id, "subjectCode": subjectCode}
               ]
          }).sort("year", -1))

          if subjects:
               print("No subjects", subjects)
               for subject in subjects:
                    subject["id"] = str(subject["_id"])
                    subject["editingTeacher"] = str(subject["editingTeacher"])
                    subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])

               return subjects
          else:
               print("There are no subjects")
               return None

     # get subject details by subjectCode, year and user id as a list
     def get_subject_by_subjectCode_year_userId(self, request: Request, user_id: str, subjectCode: str, year:int) -> Subject:
          print("This is user id", user_id)
          print("This is subjectCode", subjectCode)
          print("This is year", year)
          
          subject = list(self.get_collection(request).find({
               "$or": [
                    {"editingTeacher": user_id, "subjectCode": subjectCode, "year": year},
                    {"nonEditingTeacher": user_id, "subjectCode": subjectCode, "year": year}
               ]
          }))

          if subject:
               print("There is subjects", subject)
               for subject in subject:
                    subject["id"] = str(subject["_id"])
                    subject["editingTeacher"] = str(subject["editingTeacher"])
                    subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])

               return subject
          else:
               print("There are no subjects")
               return None


     # get subject by subjectCode as a list
     def get_subject_by_subjectCode(self, request: Request, subjectCode: str) -> list:
          print("This is subjectCode", subjectCode)
          
          subjects = list(self.get_collection(request).find({"subjectCode": subjectCode}).sort("year", -1))

          if subjects:
               print("No subjects", subjects)
               for subject in subjects:
                    subject["id"] = str(subject["_id"])
                    subject["editingTeacher"] = str(subject["editingTeacher"])
                    subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])

               return subjects
          else:
               print("There are no subjects")
               return None

     
     
     def subject_by_id(self, request: Request, id: str) -> Subject:
          subject = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if subject:
               subject["id"] = str(subject["_id"])
               subject["editingTeacher"] = str(subject["editingTeacher"])
               subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
               return subject
          
     # get subject by subjectId and UserId
     def get_subject_by_id_user_id(self, request: Request, user_id: str, id: str) -> Subject:
          subject = self.get_collection(request).find_one({
               "$and": [
                    {"_id": ObjectId(id)},
                    {
                         "$or": [
                              {"editingTeacher": user_id},
                              {"nonEditingTeacher": user_id}
                         ]
                    }
               ]
          })

          if subject:
               subject["id"] = str(subject["_id"])
               subject["editingTeacher"] = str(subject["editingTeacher"])
               subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
               # Add more fields conversion here if needed
               return subject
          else:
               return None


     def delete_subject(self, request: Request, id: str):
          subject = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})
          
     # get subject by subjectCode and year
     def get_subject_by_year_subjectCode(self,request:Request,year:int, subjectCode:str) -> Subject:
          subject = self.get_collection(request).find_one({"year": year, "subjectCode":subjectCode})
          if subject:
               subject["id"] = str(subject["_id"])
               subject["editingTeacher"] = str(subject["editingTeacher"])
               subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])
               return subject
          else:
               return None
          

          
     
     # def get_subject_teacher(self, request: Request, id: str) -> list:
     #      teacher_id = id

     #      subjects_cursor = self.get_collection(request).aggregate([
     #           {
     #                "$match": {
     #                     "$or": [
     #                          {"editingTeacher": teacher_id},
     #                          {"nonEditingTeacher": teacher_id}
     #                     ]
     #                }
     #           },
     #           { "$sort": { "createdDate": 1 } },
     #           {
     #                "$group": {
     #                     "_id": None,
     #                     "subjects": { "$push": "$$ROOT" }
     #                }
     #           }
     #      ])

     #      # Convert CommandCursor to a list
     #      subjects = list(subjects_cursor)

     #      # Convert ObjectId to string for compatibility with the existing code
     #      for subject_data in subjects:
     #           for subject in subject_data["subjects"]:
     #                subject["_id"] = str(subject["_id"])
     #                subject["editingTeacher"] = str(subject["editingTeacher"])
     #                subject["nonEditingTeacher"] = str(subject["nonEditingTeacher"])

     #      new_subjects = subjects[0]["subjects"] if subjects else []
     #      return new_subjects



     

     async def add_new_subject(self, request: Request, new_subject: SubjectCreate) -> Optional[Subject]:
          result = self.get_collection(request).insert_one(dict(new_subject))
          # print("This is result",result)
          if result.inserted_id:
               # print(result.inserted_id)
               inserted_subject = self.get_collection(request).find_one({"_id": result.inserted_id})
               if inserted_subject:
                    inserted_subject["id"] = str(inserted_subject["_id"])
                    inserted_subject["editingTeacher"] = str(inserted_subject["editingTeacher"])
                    inserted_subject["nonEditingTeacher"] = str(inserted_subject["nonEditingTeacher"])
                    return Subject(**inserted_subject)
          return None
