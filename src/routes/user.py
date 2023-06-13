from fastapi import APIRouter, Path
from bson.objectid import ObjectId

from config.database import Database
from models.user import User
from schemas.user import userEntity, usersEntity

database = Database()
db = database.connect()
users_collection = db["users"]
router = APIRouter(prefix="/users")

@router.get('/', response_description="Get all users")
async def get_all():
     users = usersEntity(users_collection.find())
     return {"status": 200, "users": users}


@router.post("/create", response_description="Create new user")
async def create_user(user: User):
     _id = users_collection.insert_one(dict(User))
     user = usersEntity(users_collection.find({"_id": _id.inserted_id}))
     return {"user": user}

@router.get('/{id}', response_description="Get a user by id")
async def get_by_id(id: str):
     user = userEntity(users_collection.find_one({"_id": ObjectId(id)}))
     return {"user": user}


@router.get("/admin", response_description="Get all admin users")
async def get_admins():
     admins = usersEntity(users_collection.find({"isAdmin": True}))
     return {"admins": admins}