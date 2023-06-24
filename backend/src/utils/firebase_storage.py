import pyrebase
import uuid
from fastapi import File,UploadFile
from io import BytesIO

firebase_config = {
  "apiKey": "AIzaSyAijhFV9Y2hKxOfZsikHfQyXPE-eSRwKZg",
  "authDomain": "papermarkin.firebaseapp.com",
  "projectId": "papermarkin",
  "storageBucket": "papermarkin.appspot.com",
  "messagingSenderId": "529261970661",
  "appId": "1:529261970661:web:7b9e613f7d71e0cf1d800c",
  "measurementId": "G-852GDJS8LT",
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