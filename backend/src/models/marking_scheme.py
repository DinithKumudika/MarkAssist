from fastapi import Request
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from typing import Optional
from pymongo import ReturnDocument
from config.database import Database
from schemas.marking_scheme import MarkingScheme , MarkingSchemeCreate, MarkingSchemeUpdate

class MarkingSchemeModel():
     collection: str = "marking_schemes"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_marking_schemes(self, request: Request) -> list:
          marking_schemes = list(self.get_collection(request).find())
          for marking_scheme in marking_schemes:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_schemes
     
     def by_id(self, request:Request, id: str)->MarkingScheme:
          marking_scheme = self.get_collection(request).find_one({'_id': ObjectId(id)})
          if marking_scheme:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
          return marking_scheme
     
     def get_marking_scheme_by_id(self, request:Request, id:str)->MarkingScheme:
          id = ObjectId(id)
          marking_scheme = list(self.get_collection(request).find({'_id': id}))
          if marking_scheme:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
               return marking_scheme
          else:
               return None
     
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
     
     # get marking scheme by year and subjectId
     def get_marking_scheme_by_year_subjectId(self, request:Request, year:int, subjectId:str) -> MarkingScheme:
          marking_scheme = self.get_collection(request).find_one({'year': year, 'subjectId': subjectId})
          if marking_scheme:
               marking_scheme["id"] = str(marking_scheme["_id"]) 
               marking_scheme["subjectId"] = str(marking_scheme["subjectId"]) 
               return marking_scheme
          else:
               print("No marking scheme")
               return None
     

     async def add_new_marking(self, request: Request, marking: MarkingSchemeCreate) -> MarkingScheme:
          # new_marking = self.get_collection(request).insert_one(marking.dict())
          new_marking = self.get_collection(request).insert_one(jsonable_encoder(marking))

          inserted_id = new_marking.inserted_id
          inserted_marking = self.get_collection(request).find_one({"_id": inserted_id})
          if inserted_marking:
               inserted_marking["id"] = str(inserted_marking["_id"])
               inserted_marking["subjectId"] = str(inserted_marking["subjectId"])
               # print("This is id",str(inserted_id));   
               return inserted_marking
          return None

     
     def update_existing_marking(self, request: Request, markingId:str , markingUrl: MarkingSchemeUpdate) -> Optional[MarkingScheme]:
          updated_marking = self.get_collection(request).find_one_and_update(
               {"_id": ObjectId(markingId)},
               {"$set": jsonable_encoder(markingUrl)},
               return_document=ReturnDocument.AFTER
          )

          if updated_marking:
               updated_marking["id"] = str(updated_marking["_id"])
               updated_marking["subjectId"] = str(updated_marking["subjectId"])
               return updated_marking
          return None
     
     
     def update(self, request: Request, filter: str, value: str | ObjectId, data)-> MarkingScheme | bool:
          updated_scheme = self.get_collection(request).find_one_and_update(
               {filter : value}, 
               {'$set': data},
               return_document=ReturnDocument.AFTER
          )
          
          if updated_scheme:
               return updated_scheme
          else:
               return False
     
     
     def delete_single(self, request: Request, field: str, value: str):
          if(field == "_id"):
               self.get_collection(request).delete_one({field: ObjectId(value)})
               deleted_scheme = self.get_collection(request).find_one({field: ObjectId(value)})
          else:
               self.get_collection(request).delete_one({field: value})
               deleted_scheme = self.get_collection(request).find_one({field: value})
          
          
          if deleted_scheme:
               return False
          else:
               return True
