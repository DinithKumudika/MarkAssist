from pydantic import BaseSettings
from dotenv import dotenv_values

env = dotenv_values("../../.env")

class CommonSettings(BaseSettings):
     APP_NAME: str = "paper marker API"
     DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
     HOST: str = "127.0.0.1"
     PORT: int = 8000

class GoogleServiceSettings(BaseSettings):
     GOOGLE_APPLICATION_CREDENTIALS: str = './../venv/service_account.json'
     FIREBASE_API_KEY: str = env.get('API_KEY')
     FIRESTORE_BUCKET: str = env.get('STORAGE_BUCKET')


class DatabaseSettings(BaseSettings):
     DB_URI: str = env.get("MONGO_URI")
     DB_NAME: str = "test"


class Settings(CommonSettings, ServerSettings, DatabaseSettings, GoogleServiceSettings):
     pass


settings = Settings()