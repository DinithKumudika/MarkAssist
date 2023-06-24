from pydantic import BaseSettings
from dotenv import dotenv_values

env = dotenv_values("../.env")

class CommonSettings(BaseSettings):
     APP_NAME: str = env.get('PROJECT_NAME')
     DEBUG_MODE: bool = True
     SECRET_KEY: str = env.get("SECRET_KEY")


class ServerSettings(BaseSettings):
     HOST: str = env.get('HOST')
     PORT: int = env.get('PORT')

class GoogleServiceSettings(BaseSettings):
     GOOGLE_APPLICATION_CREDENTIALS: str = './../venv/service_account.json'
     FIREBASE_API_KEY: str = env.get('API_KEY')
     FIRESTORE_BUCKET: str = env.get('STORAGE_BUCKET')


class DatabaseSettings(BaseSettings):
     DB_URI: str = env.get('MONGO_URI')
     DB_NAME: str = env.get('DB_NAME')


class Settings(CommonSettings, ServerSettings, DatabaseSettings, GoogleServiceSettings):
     pass


settings = Settings()