from fastapi import Request
from bson.objectid import ObjectId
from pymongo import UpdateMany

from schemas.marking import Marking, MarkingCreate

class MarkingModel():
     collection: str = "markings"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     
     def save_marking(self, request: Request, marking: MarkingCreate):
          new_marking = self.get_collection(request).insert_one(marking.dict())
          
          if new_marking:
               return new_marking.inserted_id
     
     
     def get_by_id(self, request: Request, id: str)->Marking:
          answer = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if answer:
               answer["id"] = str(answer["_id"])
               return answer
          
          
     def get_by_subject(self, request: Request, subjectId: str):
          markings = list(self.get_collection(request).find({"subjectId": subjectId}))
          
          if markings:
               for marking in markings:
                    marking["id"] = str(marking["_id"])
               return markings
          return None
     
     
     def get_by_marking_scheme(self, request: Request, schemeId: str)->list:
          markings = list(self.get_collection(request).find({"markingScheme": schemeId}))
          if markings:
               for marking in markings:
                    marking["id"] = str(marking["_id"])
               return markings
          return None
     
     
     def update():
          pass
     
     
     def update_single():
          pass
     
     def update_multiple(self, request: Request, update_data: list):
          updated_schemes = self.get_collection(request).bulk_write([
               UpdateMany(update["filter"], update["update"]) for update in update_data
          ])
          
          if updated_schemes:
               return updated_schemes.modified_count
          else:
               return False

     
     def delete_single(self, request: Request, field: str, value: str):
          if field == "_id":
               deleted_marking = self.get_collection(request).delete_one({field: ObjectId(value)})
          else:
               deleted_marking = self.get_collection(request).delete_one({field: value})
          
          if deleted_marking.deleted_count == 1:
               return True
          
          return False
     
     
     def delete(self, request: Request, field: str, value: str):
          deleted_markings = self.get_collection(request).delete_many({field: value})
          
          if deleted_markings:
               return deleted_markings.deleted_count
          return False