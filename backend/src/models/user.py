from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from config.database import Database
from schemas.user import User, UserCreate

class UserModel():
     collection: str = "users"
     
     def get_collection(self, request: Request):
          return request.app.mongodb[self.collection]
     
     def list_users(self, request: Request) -> list:
          users = list(self.get_collection(request).find())
          for user in users:
               user["id"] = str(user["_id"]) 
          return users
     
     def create_user(self, request: Request, user: UserCreate):
          new_user = self.get_collection(request).insert_one(user.dict())
          
          if new_user:
               return new_user.inserted_id
     
     def by_id(self, request: Request, id: str) -> User:
          user = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if user:
               user["id"] = str(user["_id"])
               return user
     
     def by_email(self, request: Request, email: str) -> User:
          user = self.get_collection(request).find_one({"email": email})
          if user:
               user["id"] = str(user["_id"])
               return user

     def delete(self, request: Request, id: str):
          user = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})
          
          if user:
               return True
          else:
               return False