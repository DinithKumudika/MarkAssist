from pydantic import BaseSettings
from dotenv import dotenv_values

env = dotenv_values("../../.env")

class CommonSettings(BaseSettings):
     APP_NAME: str = "paper marker API"
     DEBUG_MODE: bool = True
     IMAGE_DIR: str = "../data/images/"
     CROPPED_ANSWERS_DIR: str = "../data/answers/"
     
class ServerSettings(BaseSettings):
     HOST: str = "127.0.0.1"
     PORT: int = env["PORT"]

class ServiceSettings(BaseSettings):
     GOOGLE_APPLICATION_CREDENTIALS: str = './../venv/service_account.json'

class DatabaseSettings(BaseSettings):
     DB_URI: str = env["MONGO_URI"]
     DB_NAME: str = "test"
     
class Settings(CommonSettings, ServerSettings, ServiceSettings, DatabaseSettings):
     pass

settings = Settings()