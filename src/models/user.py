from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from config.database import Database
from schemas.user import User

class UserModel():
     collection: str = "users"
     
     def get_collection(self, request: Request):
          return request.app.mongodb[self.collection]
     
     def list_users(self, request: Request) -> list:
          users = list(self.get_collection(request).find())
          for user in users:
               user["id"] = str(user["_id"]) 
          return users
     
     def by_id(self, request: Request, id: str) -> User:
          user = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if user:
               user["id"] = str(user["_id"])
               return user
     
     def delete(self, request: Request, id: str):
          user = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})