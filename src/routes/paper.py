from fastapi import APIRouter
from fastapi.params import Body
from bson.objectid import ObjectId
import cv2
import numpy as np
from google.cloud import vision

import os

from config import config

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
     return {"status": 200, "papers": papers}


# get paper by id
@router.get("/{paper_id}", response_description="Get a paper by id")
async def get_by_id(paper_id):
     paper = paperEntity(papers_collection.find_one({"_id": ObjectId(paper_id)}))
     return {"paper": paper}


@router.get("papers/user/{user_id}", response_description="Get papers by user id")
async def get_paper_by_uid(user_id):
     uid = ObjectId(user_id)
     papers = papersEntity(papers_collection.find({"user": uid}))
     return {"papers": papers}


# add pdf page images to cloud storage and save in database
@router.post("/{paper_id}/images")
async def create_images(payload: dict = Body(...)):
     paper_no = payload["paperNo"]
     return {"paper no": paper_no}


@router.get("/{paper_id}/images")
async def create_images(paper_id):
     paper = paperEntity(papers_collection.find_one({"_id": ObjectId(paper_id)}))
     # uploads\\images\\79f48a54-27cf-4ef0-84ea-061e2e2c1f41.pdf
     paper_path = paper["paper_path"]
     filename = paper_path.split("\\")[-1]
     dir = filename.split(".pdf")[0]
     
     save_path = os.path.join(config.settings.IMAGE_DIR, dir)
     
     try:
          os.mkdir(save_path)
          return {
               "save path": save_path
          }
     except OSError:
          return {"error": "error creating folder"}
     
     save_path = os.path.join(config.settings.IMAGE_DIR, dir)
     
     try:
          os.mkdir(save_path)
          images = helpers.convert_to_images("../../uploads/images/" + filename, save_path)
          return {
               "paper_no": dir,
               "no_of_images": len(images)
          }
     except OSError:
          return {"error": OSError}