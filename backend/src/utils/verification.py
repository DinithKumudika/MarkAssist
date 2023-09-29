import hashlib
from random import randbytes
from bson import ObjectId
from fastapi import HTTPException, Request, status

from schemas.user import UserVerify
from models.user import UserModel

def create_token():
    return randbytes(10)


# create email verification code
def create_verification_code(token: str):
    hashed_code = hashlib.sha256()
    hashed_code.update(token)
    return hashed_code.hexdigest()
    

