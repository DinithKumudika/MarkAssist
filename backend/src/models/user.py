from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional
from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr

from config.database import Database
from schemas.user import User, UserCreate

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