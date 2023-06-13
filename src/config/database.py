from pymongo import MongoClient
from dotenv import dotenv_values

from config import config

class Database:
     def __init__(self):
          mongo_uri = config.settings.DB_URI
          self.client = MongoClient(mongo_uri)
     
     def get_client(self):
          return self.client
     
     def connect(self):
          try:
               self.client.admin.command('ping')
               print("You successfully connected to MongoDB!")
               db = self.client[config.settings.DB_NAME]
               return db
          except Exception as e:
               print(e)


