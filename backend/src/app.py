from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie

import os

from config.config import settings
from config.database import Database
from api.api_v1.router import router


app = FastAPI(
     title=settings.APP_NAME, 
     version=settings.API_VERSION
)

origins = [
     'http://localhost:3000'
]

app.add_middleware(
     CORSMiddleware,
     allow_origins = origins, 
     allow_credentials = True, 
     allow_methods = ["*"],
     allow_headers = ["*"]
)

# register routes
app.include_router(router, prefix=settings.API_VERSION_STR)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings.GOOGLE_APPLICATION_CREDENTIALS

@app.on_event("startup")
async def app_init():
     """
          initialise crucial application services
     """
     try:
          database = Database()
          app.db = database.connect()
          app.db_client = database.get_client()
          # await init_beanie(
          #      database=app.db, 
          #      document_models=[
          #           User
          #      ]
          # ) 
          print("You successfully connected to MongoDB!")
     except ConnectionError as e:
          print(str(e))


@app.on_event("shutdown")
async def shutdown_db_client():
     app.db_client.close()


@app.get("/", tags=["Root"])
async def read_root():
     return {
          "message": "welcome to markAssist API"
     }