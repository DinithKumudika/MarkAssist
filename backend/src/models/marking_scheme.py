from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from config.database import Database
from schemas.marking_scheme import MarkingScheme ,MarkingSchemeCreate,MarkingSchemeUpdate

class MarkingSchemeModel():
     collection: str = "marking_schemes"
     
     def get_collection(self, request: Request):
          return request.app.mongodb[self.collection]
     
     def list_marking_schemes(self, request: Request) -> list:
          marking_schemes = list(self.get_collection(request).find())
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     
     def get_marking_schemes_by_id(self, request:Request, id:str)->list:
          id = ObjectId(id)
          marking_schemes = list(self.get_collection(request).find({'_id':str}))
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     
     def get_marking_schemes_by_year(self, request:Request, year:int)->list:
          marking_schemes = list(self.get_collection(request).find({'year':year}))
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     
     def get_marking_schemes_by_year_and_subject_code(self, request:Request, year:int, code:str)->list:
          marking_schemes = list(self.get_collection(request).find({'year':year,"subjectCode":code}))
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     
     def get_marking_schemes_by_year_id_code(self, request:Request, year:int, code:str, id:str)->list:
          id = ObjectId(id)
          marking_schemes = list(self.get_collection(request).find({'year':year,"subjectCode":code, "_id":id}))
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     

     def add_new_marking(self, request: Request, marking: MarkingSchemeCreate) -> MarkingScheme:
          new_marking = self.get_collection(request).insert_one(marking.dict())
          inserted_id = new_marking.inserted_id
          inserted_marking = self.get_collection(request).find_one({"_id": inserted_id})
          if inserted_marking:
               inserted_marking["id"] = str(inserted_marking["_id"])
               inserted_marking["subjectId"] = str(inserted_marking["subjectId"])
               return inserted_marking
          return None
     
     def update_existing_marking(self, request: Request, marking: MarkingSchemeUpdate) -> MarkingScheme:
          pass
     