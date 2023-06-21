from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.params import Body
from bson.objectid import ObjectId

from config.database import Database
from models.answer import Answer, extract_answers, read_answers
from schemas.answer import answerEntity, answersEntity

router = APIRouter()

@router.post("/text/{paper_no}", response_description="extract answers as text")
async def answer_to_text(request: Request, paper_no):
     try:
          no_of_answers = extract_answers(paper_no)
          return JSONResponse({
               "status": status.HTTP_201_CREATED, 
               "message": f"{no_of_answers} answers saved"
          }) 
     except OSError:
          return JSONResponse({
               "status": status.HTTP_500_INTERNAL_SERVER_ERROR, 
               "message": "couldn't extract answers"
          }) 

          
@router.get('/text/{paper_no}', response_description="save extracted answers to the database")
async def save_answers(request: Request, paper_no):
     answers = read_answers(paper_no)
     if answers:
          return JSONResponse({
               "status": status.HTTP_200_OK, 
               "answers": answers
          }) 
     else:
          return JSONResponse({
               "status": status.HTTP_500_INTERNAL_SERVER_ERROR, 
               "message": "error getting answers"
          }) 

          
@router.post('/compare', response_description="compare between question text and marking scheme then returns similarity")
async def check_similarity():
     pass