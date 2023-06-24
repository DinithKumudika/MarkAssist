import uvicorn

from config.config import settings

if __name__ == "__main__":
     uvicorn.run(
          "app:app", 
          host= settings.HOST,
          reload = settings.DEBUG_MODE,
          port = settings.PORT
     )