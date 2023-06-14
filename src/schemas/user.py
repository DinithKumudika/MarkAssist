def userEntity(item) -> dict:
     return {
          "id": str(item["_id"]),
          "first_name": item["firstName"],
          "last_name": item["lastName"],
          "email": item["email"],
          "password": item["password"],
          "user_type": item["userType"],
          "email_active": item["emailActive"],
          "is_deleted": item["isDeleted"]
     }
     
def usersEntity(entity) -> list:
     return [userEntity(item) for item in entity]