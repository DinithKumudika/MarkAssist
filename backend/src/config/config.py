from pydantic import BaseSettings
from dotenv import dotenv_values

env = dotenv_values("../.env")

class CommonSettings(BaseSettings):
     API_VERSION_STR: str = "/api_v1"
     API_VERSION: str = "1.0.0"
     APP_NAME: str = env.get('PROJECT_NAME')
     DEBUG_MODE: bool = True
     JWT_SECRET_KEY: str = env.get("JWT_SECRET_KEY")
     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
     REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
     OPENAI_API_KEY: str = env.get('OPENAI_API_KEY')
     
     class Config:
          case_sensitive = True


class ServerSettings(BaseSettings):
     HOST: str = env.get('HOST')
     PORT: int = env.get('PORT')
     
     class Config:
          case_sensitive = True

class GoogleServiceSettings(BaseSettings):
     GOOGLE_APPLICATION_CREDENTIALS: str = '../service_account.json'
     FIREBASE_API_KEY: str = env.get('API_KEY')
     FIREBASE_AUTH_DOMAIN: str = env.get('AUTH_DOMAIN')
     FIREBASE_PROJECT_ID: str = env.get('PROJECT_ID')
     FIREBASE_BUCKET: str = env.get('STORAGE_BUCKET')
     FIREBASE_SENDER_ID: str = env.get('MESSAGING_SENDER_ID')
     FIREBASE_APP_ID: str = env.get('APP_ID')
     FIREBASE_MEASUREMENT_ID: str = env.get('MEASUREMENT_ID')
     
     class Config:
          case_sensitive = True


class DatabaseSettings(BaseSettings):
     DB_URI: str = env.get('MONGO_URI')
     DB_NAME: str = env.get('DB_NAME')
     
     class Config:
          case_sensitive = True


class Settings(CommonSettings, ServerSettings, DatabaseSettings, GoogleServiceSettings):
     pass


settings = Settings()