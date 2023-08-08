from typing import List
from fastapi import APIRouter, HTTPException, Request, status, UploadFile
from fastapi.responses import JSONResponse

import os

from schemas.answer import AnswerCreate, Answer
from models.answer import AnswerModel, extract_answers, read_answers
from models.marking import MarkingModel
from helpers import get_images, text_similarity
from utils.firebase_storage import upload_file2

router = APIRouter()
answer_model = AnswerModel()
marking_model = MarkingModel()


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
               uploadUrl= file_url,
               accuracy=None,
               keywordsaccuracy=None,
               marks= None
          )
          answer_id = answer_model.save_answer(request, answer)
          
     return JSONResponse({
               "detail": "answers saved",
               "data": urls
          }, 
          status_code=status.HTTP_201_CREATED
     )


@router.get('/compare/{markingSchemeId}', response_description="compare between question text and marking scheme then returns similarity")
async def check_similarity(request: Request, markingSchemeId:str, sub: str, stu: str):
     print("marking scheme id", markingSchemeId)
     print("student id", stu)
     print("sub id", sub)
     answers_by_student = answer_model.get_by_subject_student(request, stu, sub)
     # sorting student answers by question no's
     answers_by_student = sorted(answers_by_student, key=lambda x:int(x["questionNo"]))
     
     markings_by_scheme_id = marking_model.get_by_marking_scheme(request, markingSchemeId)
     # sorting marking scheme answers by question no's
     markings_by_scheme_id = sorted(markings_by_scheme_id, key=lambda x:int(x["questionNo"]))
     
     # print("no of student answers",answers_by_student)
     # print("no of marking answers", markings_by_scheme_id)
     
     percentages = []
     for i, el in enumerate(answers_by_student):
          keywordsAccuracy=0
          # print("student answer", i+1, ":", answers_by_student[i]["text"])
          # print("Marking answer", i+1, ":", markings_by_scheme_id[i]["text"])

          if(markings_by_scheme_id[i]["selected"]):
               percentage = text_similarity(markings_by_scheme_id[i]["text"], answers_by_student[i]["text"])
               print("Percentage:",percentage)
               
               # here we should by questionNo,userId,subjectId
               filters = {"userId":stu, "questionNo":str(i+1), "subjectId":sub}
               data = {"accuracy":percentage.split(": ")[-1]}
               # data = {"accuracy":"0.6"}
               print("filters", data)

               # # keywordsAccuracy
               # result_string = ' '.join(markings_by_scheme_id[i]["keywords"])
               # no_keywords= len(markings_by_scheme_id[i]['keywords'])
               # print("no_keywords",no_keywords)
               # keywords=[]
               # for keyword in markings_by_scheme_id[i]["keywords"]:
               #      print("keyword",keyword)
               #      if keyword.lower() in answers_by_student[i]["text"].lower():
               #          print(f"'{keyword}' is present in the paragraph.")
               #          if keyword in keywords:
               #               print(keywords)
               #           #     pass
               #          else:
               #               print("Keywords::",keywords)
               #               keywords.append(keyword)
               #               keywordsAccuracy+=100/no_keywords
               #      else:
               #          print(f"'{keyword}' is not present in the paragraph.")
               
               # answer_model.update(request, filters , data)
               print("keywordsAccuracy",keywordsAccuracy)
               
               # TODO: add to db,accuracy field add to schema
               
               percentages.append({
                    "subjectId":sub,
                    "userId":stu,
                    "questionNoquestion": i+1, 
                    # "accuracy": percentage.split(": ")[-1]
                    # "accuracy": "0.6"
               })
     return JSONResponse({
               "similarity percentages": percentages
          },
          status_code=status.HTTP_200_OK
     )
     
     
@router.post('/similarity/{answerId}')
async def save_similarity_percentage(request: Request):
     pass