from fastapi import Request
from bson.objectid import ObjectId

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
     
     def get_by_marking_scheme(self, request: Request, schemeId: str)->list:
          markings = list(self.get_collection(request).find({"markingScheme": schemeId}))
          if markings:
               for marking in markings:
                    marking["id"] = str(marking["_id"])
               return markings
          return None