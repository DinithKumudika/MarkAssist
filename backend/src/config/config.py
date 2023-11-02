from pydantic import BaseSettings
from dotenv import dotenv_values
import os

# env = dotenv_values("../.env")

class CommonSettings(BaseSettings):
     API_VERSION_STR: str = "/api_v1"
     API_VERSION: str = "1.0.0"
     DEBUG_MODE: bool = True
     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
     REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
     JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
     APP_NAME: str = os.getenv('PROJECT_NAME')
     OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
     AZURE_API_KEY:str = os.getenv('AZURE_API_KEY')
     AZURE_ENDPOINT:str = os.getenv('AZURE_ENDPOINT')
     
     # APP_NAME: str = env.get('PROJECT_NAME')
     # JWT_SECRET_KEY: str = env.get("JWT_SECRET_KEY")
     # OPENAI_API_KEY: str = env.get('OPENAI_API_KEY')
     # AZURE_API_KEY:str = env.get('AZURE_API_KEY')
     # AZURE_ENDPOINT:str = env.get('AZURE_ENDPOINT')

     class Config:
          case_sensitive = True


class ServerSettings(BaseSettings):
     HOST: str = os.getenv('HOST')
     PORT: int = os.getenv('PORT')
     
     # HOST: str = env.get('HOST')
     # PORT: int = env.get('PORT')

     class Config:
          case_sensitive = True


class GoogleServiceSettings(BaseSettings):
     # OAUTH_CLIENT_ID: str = os.getenv('GOOGLE_CLIENT_ID')
     # OAUTH_CLIENT_SECRET: str = os.getenv('GOOGLE_CLIENT_SECRET')
     GOOGLE_APPLICATION_CREDENTIALS: str = '../service_account.json'
     FIREBASE_API_KEY: str = os.getenv('API_KEY')
     FIREBASE_AUTH_DOMAIN: str = os.getenv('AUTH_DOMAIN')
     FIREBASE_PROJECT_ID: str = os.getenv('PROJECT_ID')
     FIREBASE_BUCKET: str = os.getenv('STORAGE_BUCKET')
     FIREBASE_SENDER_ID: str = os.getenv('MESSAGING_SENDER_ID')
     FIREBASE_APP_ID: str = os.getenv('APP_ID')
     FIREBASE_MEASUREMENT_ID: str = os.getenv('MEASUREMENT_ID')
     
     # OAUTH_CLIENT_ID: str = env.get('GOOGLE_CLIENT_ID')
     # OAUTH_CLIENT_SECRET: str = env.get('GOOGLE_CLIENT_SECRET')
     # FIREBASE_API_KEY: str = env.get('API_KEY')
     # FIREBASE_AUTH_DOMAIN: str = env.get('AUTH_DOMAIN')
     # FIREBASE_PROJECT_ID: str = env.get('PROJECT_ID')
     # FIREBASE_BUCKET: str = env.get('STORAGE_BUCKET')
     # FIREBASE_SENDER_ID: str = env.get('MESSAGING_SENDER_ID')
     # FIREBASE_APP_ID: str = env.get('APP_ID')
     # FIREBASE_MEASUREMENT_ID: str = env.get('MEASUREMENT_ID')

     
     class Config:
          case_sensitive = True


class AzureServiceSettings(BaseSettings):
     VISION_API_KEY: str = os.getenv('AZURE_API_KEY')
     VISION_ENDPOINT: str = os.getenv('AZURE_ENDPOINT')
     
     # VISION_API_KEY: str = env.get('AZURE_API_KEY')
     # VISION_ENDPOINT: str = env.get('AZURE_ENDPOINT')



class DatabaseSettings(BaseSettings):
     DB_URI: str = os.getenv('MONGO_URI')
     DB_NAME: str = os.getenv('DB_NAME')
     
     # DB_URI: str = env.get('MONGO_URI')
     # DB_NAME: str = env.get('DB_NAME')

     class Config:
          case_sensitive = True
          

class MailSettings(BaseSettings):
     MAIL_USERNAME :str = os.getenv('MAIL_USERNAME')
     MAIL_PASSWORD :str = os.getenv('MAIL_PASSWORD')
     MAIL_FROM :str = os.getenv('MAIL_FROM')
     MAIL_PORT :int = int(os.getenv('MAIL_PORT'))
     MAIL_SERVER :str = os.getenv('MAIL_SERVER')
     MAIL_FROM_NAME :str = os.getenv('MAIN_FROM_NAME')
     
     # MAIL_USERNAME :str = env.get('MAIL_USERNAME')
     # MAIL_PASSWORD :str = env.get('MAIL_PASSWORD')
     # MAIL_FROM :str = env.get('MAIL_FROM')
     # MAIL_PORT :int = int(env.get('MAIL_PORT'))
     # MAIL_SERVER :str = env.get('MAIL_SERVER')
     # MAIL_FROM_NAME :str = env.get('MAIN_FROM_NAME')

     
     class Config:
          case_sensitive = True


class Settings(CommonSettings, ServerSettings, DatabaseSettings, GoogleServiceSettings, AzureServiceSettings, MailSettings):
     pass


settings = Settings()