import uvicorn

from config import config

if __name__ == "__main__":
     uvicorn.run(
          "app:app", 
          host= config.settings.HOST,
          reload = config.settings.DEBUG_MODE,
          port = config.settings.PORT
     )