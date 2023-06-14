from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body
from bson.objectid import ObjectId
import cv2
import numpy as np
from google.cloud import vision
import httpx

import os

from config.database import Database
from models.paper import Paper
from schemas.paper import paperEntity, papersEntity
import helpers

database = Database()
db = database.connect()
papers_collection = db["tickets"]
router = APIRouter(prefix="/papers")

@router.get("/", response_description="Get all papers")
async def get_all_papers():
     papers = papersEntity(papers_collection.find())
     if papers:
          return {"status": 200, "papers": papers}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="No papers to show"
     )


# get paper by id
@router.get("/{paper_id}", response_description="Get a paper by id")
async def get_by_id(paper_id):
     paper = paperEntity(papers_collection.find_one({"_id": ObjectId(paper_id)}))
     if paper:
          return {"paper": paper}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )


@router.get("/download/{paper_id}", response_description="Download paper from cloud storage")
async def download_paper(paper_id):
     paper = paperEntity(papers_collection.find_one({"_id": ObjectId(paper_id)}))
     
     if paper:
          document_url = paper["paper_path"]
     
          async with httpx.AsyncClient() as client:
               response = await client.get(document_url)
               response.raise_for_status()
               save_path = f"./../data/papers/{paper_id}.pdf"
               with open(save_path, "wb") as file:
                    file.write(response.content)
          try:
               dir_path = os.path.join('./../data/images/', paper_id)
               os.mkdir(dir_path)
               images = helpers.convert_to_images(save_path, dir_path)
               
               return {
                    "message": "ok", 
                    "paper_path": document_url,
                    "images_created": len(images)
               }
          except OSError:
               return {"error": OSError}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )


@router.get("/user/{user_id}", response_description="Get papers by user id")
async def get_paper_by_uid(user_id):
     uid = ObjectId(user_id)
     papers = papersEntity(papers_collection.find({"user": uid}))
     if papers:
          return {"papers": papers}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"No papers related to user with id of {user_id}"
     )


# add pdf page images to cloud storage and save in database
@router.post("/{paper_id}/images")
async def create_images(payload: dict = Body(...)):
     paper_no = payload["paperNo"]
     return {"paper no": paper_no}


@router.get("/{paper_id}/images")
async def create_images(paper_id):
     paper = paperEntity(papers_collection.find_one({"_id": ObjectId(paper_id)}))
     paper_path = paper["paper_path"]