import pyrebase
import uuid
from fastapi import File,UploadFile
from io import BytesIO
import os

from config.config import settings

firebase_config = {
  "apiKey": settings.FIREBASE_API_KEY,
  "authDomain": settings.FIREBASE_AUTH_DOMAIN,
  "projectId": settings.FIREBASE_PROJECT_ID,
  "storageBucket": settings.FIREBASE_BUCKET,
  "messagingSenderId": settings.FIREBASE_SENDER_ID,
  "appId": settings.FIREBASE_APP_ID,
  "measurementId": settings.FIREBASE_MEASUREMENT_ID,
  "databaseURL": "" 
}

firebase = pyrebase.initialize_app(firebase_config)
fb_storage = firebase.storage()


async def upload_file(file: UploadFile, file_name: str):
    file_extension = file.filename.split(".")[-1]  # Get the file extension
    unique_filename = f"{uuid.uuid4()}_{file_name}.{file_extension}"  # Generate a unique file name
    upload_path = f"uploads/pdf/{unique_filename}"
    file_content = await file.read()
    file_bytes = BytesIO(file_content)
    renamed_file = UploadFile(filename=unique_filename, file=file_bytes)  # Create a new UploadFile instance with the renamed file
    fb_storage.child(upload_path).put(renamed_file.file)
    download_url = fb_storage.child(upload_path).get_url(None)
    return download_url

async def upload_file2(image: UploadFile, path: str, folder: str, image_name: str):
    file_extension = image.filename.split(".")[-1]  # Get the file extension
    unique_filename = f"{uuid.uuid4()}_{image_name}.{file_extension}"  # Generate a unique file name
    upload_path = os.path.join(f"{path}/{folder}/", unique_filename) 
    file_content = await image.read()
    file_bytes = BytesIO(file_content)
    renamed_file = UploadFile(filename=unique_filename, file=file_bytes)  # Create a new UploadFile instance with the renamed file
    fb_storage.child(upload_path).put(renamed_file.file)
    download_url = fb_storage.child(upload_path).get_url(None)
    return download_url
  
async def save_file_to_local():
  pass