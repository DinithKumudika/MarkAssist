from fastapi import FastAPI

import uvicorn

from bson.objectid import ObjectId
from typing import Optional

from config.database import Database
from config import config

# routes
import routes.user as user_router

# schemas
from schemas.paper import paperEntity, papersEntity
from schemas.answer import answerEntity, answersEntity

from scripts.text import preprocess, compare

app = FastAPI()
app.include_router(user_router.router)

@app.on_event("startup")
async def startup_db_client():
     database = Database()
     app.mongodb = database.connect()
     app.mongodb_client = database.get_client()


@app.on_event("shutdown")
async def shutdown_db_client():
     app.mongodb_client.close()


@app.get("/")
async def home():
     return {
          "message": "marker assist API"
     }





if __name__ == "__main__":
     uvicorn.run(
          "main:app", 
          host= config.settings.HOST,
          reload = config.settings.DEBUG_MODE,
          port = config.settings.PORT
     )