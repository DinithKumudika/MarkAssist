from  schemas.user import UserCreate
from models.user import User as UserModel

class UserService:
     @staticmethod
     async def create_user(user: UserCreate):
          pass