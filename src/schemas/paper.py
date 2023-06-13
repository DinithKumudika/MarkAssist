def paperEntity(item) -> dict:
     return {
          "id": str(item["_id"]),
          "user": str(item["user"]),
          "description": item["description"],
          "paper_path": item["paper"],
          "marking_scheme_path": item["markingScheme"]
     }

def papersEntity(entity) -> list:
     return [paperEntity(item) for item in entity]