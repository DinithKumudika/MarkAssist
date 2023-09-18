from fastapi import Request
from bson.objectid import ObjectId
from typing import Optional,Dict,List, Union
from config.database import Database
from schemas.paper import Paper,PaperCreate,PaperForm
from pymongo import ReturnDocument


class PaperModel():
     collection: str = "papers"
     
     def get_collection(self, request: Request):
          return request.app.db[self.collection]
     
     def list_papers(self, request: Request) -> list:
          papers = list(self.get_collection(request).find())
          for paper in papers:
               paper["id"] = str(paper["_id"])
               paper["subjectId"] = str(paper["subjectId"])  
          return papers
     
     def by_id(self, request: Request, id: str) -> Paper:
          paper = self.get_collection(request).find_one({"_id": ObjectId(id)})
          if paper:
               paper["id"] = str(paper["_id"])
               paper["subjectId"] = str(paper["subjectId"]) 
          return paper
          
     def by_user_id(self, request:Request, id:str) -> list:
          papers = list(self.get_collection(request).find({"user": ObjectId(id)}))

          for paper in papers:
               paper["id"] = str(paper["_id"])
               paper["subjectId"] = str(paper["subjectId"]) 
          return papers

     def papers_by_subjectId(self,request:Request,subject_id:str) -> list:
          papers = list(self.get_collection(request).find({"subjectId": subject_id}))

          for paper in papers:
               paper["id"] = str(paper["_id"])
               paper["subjectId"] = str(paper["subjectId"]) 
          return papers
     
     def papers_by_subjectId_and_marksGenerated(self,request:Request,subject_id:str, marksGenerated:bool) -> list:
          papers = list(self.get_collection(request).find({"subjectId": subject_id, "marksGenerated": marksGenerated}))

          for paper in papers:
               paper["id"] = str(paper["_id"])
               paper["subjectId"] = str(paper["subjectId"]) 
          return papers
     
     async def add_new_paper(self, request: Request, paper: PaperCreate) -> Paper:
          new_paper = self.get_collection(request).insert_one(paper.dict())
          inserted_id = new_paper.inserted_id
          inserted_paper = self.get_collection(request).find_one({"_id": inserted_id})
          if inserted_paper:
               inserted_paper["id"] = str(inserted_paper["_id"])
               inserted_paper["subjectId"] = str(inserted_paper["subjectId"])
               # print("This is id",str(inserted_id));   
               return inserted_paper
          return None
     
     def update(self, request: Request, filters: Dict[str, Union[str, ObjectId]], data)-> Paper | bool:
          print("filters", filters)
          print("data", data)
          updated_paper = self.get_collection(request).find_one_and_update(
               filters, 
               {'$set': data},
               return_document=ReturnDocument.AFTER
          )
          
          print("updated answer", updated_paper)
          if updated_paper:
               updated_paper["id"] = str(updated_paper["_id"])
               return updated_paper
          else:
               return False
     
     
     def delete(self, request: Request, id: str):
          paper = self.get_collection(request).find_one_and_delete({"_id": ObjectId(id)})