def answerEntity(item) -> dict:
     return {
          "paper_no": str(item["paperNo"]),
          "question_no": int(item["questionNo"]),
          "text": item["text"]
     }
     
def answersEntity(entity) -> list:
     return [answerEntity(item) for item in entity]