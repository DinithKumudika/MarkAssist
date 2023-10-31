from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from pymongo import ReturnDocument

from config.database import Database
from schemas.user import User, StudentCreate, TeacherCreate
from schemas.student import Student

# class User(Document):
#      firstName: str = Field(max_length=50)
#      lastName: str = Field(max_length=50)
#      email: EmailStr
#      password: str
#      userType: str
#      emailActive: bool = Field(default=False)
#      isDeleted: bool = Field(default=False)
     
#      def __repr__(self) -> str:
#           return f"<User {self.email}>"
     
#      def __str__(self) -> str:
#           return self.email
     
#      def __hash__(self) -> int:
#           return hash(self.email)
     
#      @classmethod
#      async def by_email(self, email: str) -> User:
#           return await self.find_one(self.email == email)
     
#      @classmethod
#      async def by_id(self, id: str) -> User:
#           return await self.find_one(self.id  == ObjectId(id))
     
#      class Collection:
#           name = "users"

class UserModel():
     collection: str = "users"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_users(self, request: Request) -> list:
          users = list(self.get_collection(request).find())
          for user in users:
               user["id"] = str(user["_id"]) 
          return users


     def list_teachers(self, request: Request) -> list:
          users = list(self.get_collection(request).find({'userType':'teacher'}))
          for user in users:
               user["id"] = str(user["_id"]) 
          return users


     def list_students(self, request: Request) -> list:
          users = list(self.get_collection(request).find({'userType':'student'}))
          for user in users:
               user["id"] = str(user["_id"]) 
          return users
          
     
     def find(self, request: Request, field: str, value) -> User:
          user = self.get_collection(request).find_one({field: value})
          if user:
               user["id"] = str(user["_id"])
               return user
     
     # create student model and add this to it
     def get_student_by_index(self, request: Request, indexNo: int) -> Student:
          student = self.get_collection(request).find_one({"studentIndex": indexNo})
          if student:
               student["id"] = str(student["_id"])
               return student
     
     
     def create_user(self, request: Request, user: StudentCreate | TeacherCreate):
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
          
          
     def update_single(self, request: Request, filter: str, value: str | ObjectId, data):
          updated_user = self.get_collection(request).find_one_and_update(
               {filter : value}, 
               {'$set': data},
               return_document=ReturnDocument.AFTER
          )
          
          if updated_user:
               return updated_user
          else:
               return False
          

     def delete(self, request: Request, id: str):
          user = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})
          
          if user:
               return True
          else:
               return False
     