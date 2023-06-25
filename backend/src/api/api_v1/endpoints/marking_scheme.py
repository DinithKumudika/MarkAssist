from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body
from bson.objectid import ObjectId

from config.database import Database
from models.marking_scheme import MarkingScheme

database = Database()
db = database.connect()
marking_scheme_collection = db["tickets"]
router = APIRouter(prefix="marking")

@router.get("/", response_description="Get all marking schemes")
async def get_All():
     pass

@router.get("/{marking_id}", response_description="Get a marking scheme id")
async def get_by_id(marking_id):
     pass