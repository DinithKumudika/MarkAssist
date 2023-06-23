from pydantic import BaseModel, EmailStr

class Token(BaseModel):
     token: str
     token_type: str
     
class TokenData(BaseModel):
     user_id: str
     username: EmailStr