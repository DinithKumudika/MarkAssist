from typing import List
from fastapi import APIRouter, HTTPException, Request, status, UploadFile
from fastapi.responses import JSONResponse
from fastapi.params import Body
from bson.objectid import ObjectId

import os
from helpers import get_images

from schemas.answer import AnswerCreate, Answer
from models.answer import AnswerModel, extract_answers, read_answers
from helpers import get_images
from utils.firebase_storage import upload_file2

router = APIRouter()
answer_model = AnswerModel()

@router.get('/{paper_no}', response_description="get answer images from database", response_model=List[Answer])
async def get_answers_by_paper(request: Request, paper_no)->list:
     answers = answer_model.get_by_paper(request, paper_no)
     
     if answers:
          return answers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"No answers for paper with id of {paper_no}"
     )


@router.get("/image/{paper_no}", response_description="extract answers as images")
async def answer_to_text(paper_no):
     print(paper_no)
     no_of_answers = extract_answers(paper_no)
     print(no_of_answers)
     if no_of_answers:
          return JSONResponse({
               "message": f"{no_of_answers} answers saved"
               }, 
               status_code=status.HTTP_201_CREATED
          )
     else:
          return JSONResponse({
               "message": "couldn't extract answers"
               },
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
          )


@router.get("/text/{paper_no}", response_description="get extracted answer text")
async def get_text(paper_no):
     answers = read_answers(paper_no)
     
     if answers:
          return JSONResponse({
               "data": answers
               }, 
               status_code=status.HTTP_200_OK
          )
     else:
          return JSONResponse({
               "message": "error getting answers"
               },
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
          )


@router.post('/save/{paper_no}',response_description="save extracted answers to the db and cloud")
async def save_answers(request: Request, paper_no, sub, stu):
     answers = read_answers(paper_no)
     answer_images = get_images(os.path.join('../data/answers/', paper_no))
     urls = []
     
     for i, image in enumerate(answer_images):
          with open(image, "rb") as file:
               upload = UploadFile(filename=image, file=file)
               filename = f"Q_{i+1}"
               file_url = await upload_file2(upload, "uploads/images/answers/papers", paper_no, filename)
               urls.append(file_url)
          question_no = answers[i]["question no"]
          answer_text = answers[i]["text"]
          answer = AnswerCreate(
               paperNo=paper_no, 
               subjectId= sub, 
               userId=stu, 
               questionNo=question_no, 
               text=answer_text,
               uploadUrl= file_url
          )
          answer_id = answer_model.save_answer(request, answer)
          
     return JSONResponse({
               "detail": "answers saved",
               "data": urls
          }, 
          status_code=status.HTTP_201_CREATED
     )

          
@router.post('/compare', response_description="compare between question text and marking scheme then returns similarity")
async def check_similarity():
     pass