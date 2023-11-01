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
     
     def calculateGPA(self, request: Request):
          # get all student_subject collection
          student_subject_list = self.list_student_subject(request)
     
          # print("This is student_subject_list", student_subject_list)
     
          final_updated_student_subject_list = []
          # get one student's subjects list
          for student_subject in student_subject_list:
              student_subject['id'] = str(student_subject['_id'])
              gpa = 0
              total_credit = 0
              # get the student's subject list
              subjects_results_list = student_subject['subject']
              # print("\n\nThis is subjects_results_list", subjects_results_list, "\n\n")
     
              # loop through the subjects of one student
              for subject in subjects_results_list:
                  total_credit += subject['no_of_credit']
                  gpa += subject['gpv'] * subject['no_of_credit']
              gpa = gpa / total_credit
     
              # update student_subject collection
              filters = {"index": student_subject['index']}
              data = {"gpa": gpa, "total_credit": total_credit}
     
          #     print("1")
     
              updated_student_subject_collection = self.get_collection(request).find_one_and_update(
                  filters,
                  {'$set': data},
                  return_document=ReturnDocument.AFTER
              )
     
          #     print("2")
     
              # Convert ObjectId to string for serialization
              updated_student_subject_collection["id"] = str(updated_student_subject_collection["_id"])
              updated_student_subject_collection.pop("_id")
          #     print("\n\nThis is updated_student_subject_collection", updated_student_subject_collection)
          #     print("This is updated_student_subject_collection id", updated_student_subject_collection['id'], "\n\n")
              final_updated_student_subject_list.append(updated_student_subject_collection)
     
          #     print("4")
     
          return final_updated_student_subject_list
     
     def list_of_index_gpa(self, request: Request):
          # get all student_subject collection
          student_subject_list = self.list_student_subject(request)
     
          # print("This is student_subject_list", student_subject_list)
     
          final_updated_student_subject_list_of_gpa_index = []
          # get one student's subjects list
          for student_subject in student_subject_list:
              student_subject['id'] = str(student_subject['_id'])
              
              index = student_subject['index'];
              gpa = student_subject['gpa'];
              
              final_updated_student_subject_list_of_gpa_index.append({'index': index, 'gpa': gpa})
              
          # sort the final_updated_student_subject_list_of_gpa_index list
          final_updated_student_subject_list_of_gpa_index = sorted(final_updated_student_subject_list_of_gpa_index, key=lambda x: x["gpa"], reverse=True)
          
          # now update the rank of each student
          for index,student in final_updated_student_subject_list_of_gpa_index:
               # update student_subject collection
               filters = {"index": student['index']}
               data = {"rank": index+1 }
     
               updated_student_subject_collection = self.get_collection(request).find_one_and_update(
                   filters,
                   {'$set': data},
                   return_document=ReturnDocument.AFTER
               )



     
