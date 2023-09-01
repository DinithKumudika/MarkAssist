from  schemas.user import UserCreate
from models.user import User as UserModel

class UserService:
     @staticmethod
     async def create_user(user: UserCreate):
          UserModel.create(user)
          
     @staticmethod
     async def update_user():
          pass
     
     @staticmethod
     async def get_all():
          pass