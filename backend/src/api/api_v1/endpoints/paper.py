from fastapi import APIRouter, Body, HTTPException, Request, Response, status, UploadFile, File,Form,Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from io import TextIOWrapper
from datetime import datetime
import httpx
import requests

import os
import zipfile
import io

from models.paper import PaperModel
from schemas.paper import Paper,PaperCreate,PaperForm

from models.user import UserModel
from schemas.user import User

from schemas.answer import AnswerCreate, Answer
from models.answer import AnswerModel, extract_answers, read_answers ,read_answers_azure

from models.student_subject import StudentSubjectModel
from schemas.student_subject import StudentSubjectBase, StudentSubject,StudentSubjectUpdate, StudentSubjectCreate

from models.subject import SubjectModel;

from helpers import get_images, text_similarity, add_student_subject, add_subject
from utils.firebase_storage import upload_file2

from utils.auth import get_current_active_user

from utils.firebase_storage import upload_file 
import helpers

router = APIRouter()
paper_model = PaperModel()
subject_model = SubjectModel()
answer_model = AnswerModel()
user_model = UserModel()
student_subject_model = StudentSubjectModel()

@router.get("/", response_description="Get all papers", response_model=List[Paper])
async def get_all_papers(request: Request, current_user: User = Depends(get_current_active_user)):
     papers = paper_model.list_papers(request)
     if papers:
          return papers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="No papers to show"
     )


# get paper by id
@router.get("/{paper_id}", response_description="Get a paper by id", response_model=Paper)
async def get_by_id(request: Request, paper_id, current_user: User = Depends(get_current_active_user)):
     paper = paper_model.by_id(request, paper_id)
     if paper:
          return paper 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )


@router.get("/download/{paper_id}", response_description="Download paper from cloud storage")
async def download_paper(request: Request, paper_id: str):
     paper = paper_model.by_id(request, paper_id)
     
     if paper:
          document_url = paper["paperUrl"]
     
          async with httpx.AsyncClient() as client:
               response = await client.get(document_url)
               response.raise_for_status()
               save_path = f"./../data/papers/{paper_id}.pdf"
               with open(save_path, "wb") as file:
                    file.write(response.content)
          try:
               dir_path = os.path.join('./../data/images/paper', paper_id)
               os.mkdir(dir_path)
               images = helpers.convert_to_images(save_path, dir_path)
               
               return JSONResponse({
                         "paper_path": document_url,
                         "images_created": len(images)
                    },
                    status_code=status.HTTP_200_OK
               ) 
          except OSError:
               return {"error": OSError}
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"There is no paper with the id of{paper_id}"
     )

# get papers list according to subject id
@router.get("/subjects/{subject_id}", response_description="Get papers by subject id",response_model=List[Paper])
async def get_paper_by_subjectId(request: Request, subject_id:str):

     papers = paper_model.papers_by_subjectId(request,subject_id)
     if papers:
          return papers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"No papers related to subject id {subject_id}"
     )
     
     
@router.get("/user/{user_id}", response_description="Get papers by user id",response_model=List[Paper])
async def get_paper_by_uid(request: Request, user_id):
     uid = ObjectId(user_id)
     # papers = papersEntity(request.app.mongodb["tickets"].find({"user": uid}))
     papers = paper_model.by_user_id(request,uid)
     if papers:
          return papers 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail=f"No papers related to user with id of {user_id}"
     )


# add pdf page images to cloud storage and save in database
@router.post("/{paper_id}/images")
async def create_images(request:Request, payload: dict = Body(...)):
     paper_no = payload["paperNo"]
     return JSONResponse({
          "status": status.HTTP_201_CREATED, 
          "paper no": paper_no
     }) 


@router.get("/{paper_id}/images")
async def create_images(request:Request, paper_id):
     # paper = await paperEntity(request.app.mongodb["tickets"].find_one({"_id": ObjectId(paper_id)}))
     paper_id =  ObjectId(paper_id)
     paper = await paper_model.by_id(request, paper_id)
     paper_path = paper["paper"]
     
# @router.post('/upload/file/')
# async def upload_files(request: Request, files: List[UploadFile] = File(...)):
#      for file in files:
#           paper_url = await upload_file(file, file.filename)
          
#           data = {
#                "status":200,
#                "message": "File uploaded successfully",
#                "paper_url":paper_url
#           }
          
#      return "File upload success";


# @router.post('/upload/file/', response_description="Add new papers", response_model=List[Paper], status_code=status.HTTP_201_CREATED)
# async def upload_files(request: Request, files: List[UploadFile] = File(...), year: str = Form(...), subjectId: str = Form(...)):     
#      # get the subjectCode and subjectName using subjectId
#      subject = subject_model.subject_by_id(request, subjectId)
#      if subject:
#           print("There is subject")
#           # print(subject['subjectName'])
#           # print(subject['subjectCode'])
          
#           papers_created = []
          
#           for file in files:
#                print(file.filename)

#                # Upload the file and get the file URL
#                paper_url_up = await upload_file(file, file.filename)
#                print(paper_url_up)

#                # Create a new paper object with the provided data and file URL
#                paper = PaperCreate(
#                     year=year,
#                     subjectId=subjectId,
#                     subjectCode=subject['subjectCode'],
#                     subjectName=subject['subjectName'],
#                     paper=file.filename,
#                     paperUrl=paper_url_up,
#                     createdAt=datetime.now(),
#                     updatedAt=datetime.now()
#                )
#                # print(paper);

#                # Save the paper to the database using your model
#                new_paper = await paper_model.add_new_paper(request, paper)
#                if new_paper:
#                     papers_created.append(new_paper)

#           if papers_created:
#                return JSONResponse({
#                     "detail": "New papers added", 
#                     "data": [paper["id"] for paper in papers_created],
#                     "indexNos": [file.filename.split(".")[0] for file in files]
#                }, 
#                status_code=status.HTTP_200_OK
#                )

#           raise HTTPException(
#                status_code=status.HTTP_404_NOT_FOUND,
#                detail="Error in file upload"
#           )
#      else:
#           raise HTTPException(
#                status_code=status.HTTP_404_NOT_FOUND,
#                detail="Add subject First"
#           )

# @router.post('/upload/file/',response_description="Add a new paper", response_model = Paper, status_code= status.HTTP_201_CREATED)
# async def upload_files(request: Request, file: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...)):     
#      # get the subjectCode and subjectName using subjectId
#      subject = subject_model.subject_by_id(request, subjectId)
#      if(subject):
#           print("There is subject")
#           # print(subject['subjectName'])
#           # print(subject['subjectCode'])
#           print(file.filename)

#           # Upload the file and get the file URL
#           paper_url_up = await upload_file(file,file.filename)
#           print(paper_url_up)

#           # Create a new paper object with the provided data and file URL
#           paper = PaperCreate(
#                year=year,
#                subjectId=subjectId,
#                subjectCode=subject['subjectCode'],
#                subjectName=subject['subjectName'],
#                paper = file.filename,
#                paperUrl= paper_url_up,
#                createdAt =  datetime.now(),
#                updatedAt = datetime.now()
#           )
#           # print(paper);

#           # Save the paper to the database using your model
#           new_paper = await paper_model.add_new_paper(request, paper)
#           if new_paper:
#                return JSONResponse({
#                          "detail": "new paper added", 
#                          "data": new_paper["id"],
#                          "indexNo": file.filename.split(".")[0]
#                     }, 
#                     status_code=status.HTTP_200_OK
#                )

#           raise HTTPException(
#                status_code=status.HTTP_404_NOT_FOUND,
#                detail="error in file upload"
#           )
#      else:
#           raise HTTPException(
#                status_code=status.HTTP_404_NOT_FOUND,
#                detail="Add subject First"
#           )

@router.post('/upload/file/', response_description="Add new papers", response_model=List[Paper], status_code=status.HTTP_201_CREATED)
async def upload_files(request: Request, files: List[UploadFile] = File(...), year: str = Form(...), subjectId: str = Form(...)):
     # get the subjectCode and subjectName using subjectId
     print("Files::",files)
     subject = subject_model.subject_by_id(request, subjectId)
     if subject:
          print("There is subject")
          # print(subject['subjectName'])
          # print(subject['subjectCode'])

          # Check if the uploaded file is a zip file
          if files[0].filename.endswith('.zip'):
               try:
                    # Read the zip file contents into memory
                    zip_data = await files[0].read()

                    # Create an in-memory zip file object
                    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
                         # List the files in the zip archive
                         file_list = zip_ref.namelist()

                         papers_created = []
                         for extracted_file in file_list:
                              # Read the extracted file's data into memory
                              extracted_file_data = zip_ref.read(extracted_file)

                              # Upload the extracted file and get the file URL
                              paper_url_up = await upload_file(UploadFile(filename=extracted_file, file=io.BytesIO(extracted_file_data)), extracted_file)
                              print(f"Uploaded file: {extracted_file}")
                              print(f"File URL: {paper_url_up}")
                              
                              # check if user details alredy in the student_subject collection
                              index = extracted_file.split(".")[0]
                              student_subject = student_subject_model.by_index(request, index)
                              
                              if student_subject:
                                   add_subject(request,student_subject,subject,index)
                              else:
                                   new_student_subject = add_student_subject(request,subject,index)
                                   print("this is end of else", new_student_subject)
                                   
                              # Create a new paper object with the provided data and file URL
                              paper = PaperCreate(
                                   year=year,
                                   subjectId=subjectId,
                                   subjectCode=subject['subjectCode'],
                                   subjectName=subject['subjectName'],
                                   paper=extracted_file,
                                   paperUrl=paper_url_up,
                                   marksGenerated= False,
                                   createdAt=datetime.now(),
                                   updatedAt=datetime.now()
                              )
                              # print(paper);

                              # Save the paper to the database using your model
                              new_paper = await paper_model.add_new_paper(request, paper)
                              
                              if new_paper:
                                   document_url = new_paper["paperUrl"]
                                   async with httpx.AsyncClient() as client:
                                        response = await client.get(document_url)
                                        response.raise_for_status()
                                        save_path = f"./../data/papers/{new_paper['id']}.pdf"
                                        with open(save_path, "wb") as file:
                                             file.write(response.content)
                                   try:
                                        dir_path = os.path.join('./../data/images/paper', new_paper['id'])
                                        os.mkdir(dir_path)
                                        images = helpers.convert_to_images(save_path, dir_path)

                                        no_of_answers = extract_answers(new_paper['id'])
                                        print(no_of_answers)
                                        if no_of_answers:
                                             answers = read_answers_azure(new_paper['id'])
                                             if answers:
                                                 answers = read_answers_azure(new_paper['id'])
                                                 answer_images = get_images(os.path.join('../data/answers/', new_paper['id']))
                                                 urls = []

                                                 for i, image in enumerate(answer_images):
                                                      with open(image, "rb") as files:
                                                           upload = UploadFile(filename=image, file=files)
                                                           filename = f"Q_{i+1}"
                                                           file_url = await upload_file2(upload, "uploads/images/answers/papers", new_paper['id'], filename)
                                                           urls.append(file_url)
                                                      question_no = answers[i]["question no"]
                                                      answer_text = answers[i]["text"]
                                                      print("user_id:",new_paper['paper'].split(".")[0])
                                                      
                                                      answer = AnswerCreate(
                                                           paperNo=new_paper['id'], 
                                                           subjectId= new_paper['subjectId'], 
                                                           userId=new_paper['paper'].split(".")[0], 
                                                           questionNo=question_no, 
                                                           text=answer_text,
                                                           uploadUrl= file_url,
                                                           accuracy=0.0,
                                                           keywordsaccuracy=0.0,
                                                           marks= 0.0
                                                      )
                                                      answer_id = answer_model.save_answer(request, answer)
                                                      print("answer_id:",answer_id)
                                                 papers_created.append(new_paper)
                                                 print("papers_created:",papers_created)

                                             else:
                                                  return JSONResponse({
                                                       "message": "error getting answers"
                                                       },
                                                       status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                  )
                                        else:
                                             return JSONResponse({
                                                  "message": "couldn't extract answers"
                                                  },
                                                  status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                             )
                                   except OSError:
                                        return {"error": OSError}
                              else:
                                   raise HTTPException(
                                        status_code=status.HTTP_404_NOT_FOUND, 
                                        detail="Errorr in file upload"
                                   )

                              

                         if papers_created:
                              return JSONResponse({
                                   "detail": "New papers added",
                                   "data": [paper["id"] for paper in papers_created],
                                   "indexNos": [paper['paper'].split(".")[0] for paper in papers_created]
                              },
                              status_code=status.HTTP_200_OK
                              )

               except zipfile.BadZipFile:
                    raise HTTPException(
                         status_code=status.HTTP_400_BAD_REQUEST,
                         detail="Invalid zip file format"
                    )

          else:
               # Handle pdfs

               papers_created = []
               count=0
               for file in files:
                    print("count:",count)
                    print(file.filename)
                    count+=1

                    # Upload the file and get the file URL
                    paper_url_up = await upload_file(file, file.filename)
                    print(paper_url_up)
                    
                    
                    # check if user details alredy in the student_subject collection
                    index = file.filename.split(".")[0]
                    student_subject = student_subject_model.by_index(request, index)
                    print("This is student subject", student_subject)
                    
                    if student_subject:
                         add_subject(request,student_subject,subject,index)
                    else:
                         # create a new one
                         print("This is student subject else close")
                         new_student_subject = add_student_subject(request,subject,index)
                         print("this is end of else", new_student_subject)
                    
                    # Create a new paper object with the provided data and file URL
                    paper = PaperCreate(
                         year=year,
                         subjectId=subjectId,
                         subjectCode=subject['subjectCode'],
                         subjectName=subject['subjectName'],
                         paper=file.filename,
                         paperUrl=paper_url_up,
                         marksGenerated= False,
                         createdAt=datetime.now(),
                         updatedAt=datetime.now()
                    )
                    # print(paper);

                    # Save the paper to the database using your model
                    new_paper = await paper_model.add_new_paper(request, paper)
                    
                    if new_paper:
                         document_url = new_paper["paperUrl"]
                         async with httpx.AsyncClient() as client:
                              response = await client.get(document_url)
                              response.raise_for_status()
                              save_path = f"./../data/papers/{new_paper['id']}.pdf"
                              with open(save_path, "wb") as file:
                                   file.write(response.content)
                         try:
                              dir_path = os.path.join('./../data/images/paper', new_paper['id'])
                              os.mkdir(dir_path)
                              images = helpers.convert_to_images(save_path, dir_path)
                              
                              no_of_answers = extract_answers(new_paper['id'])
                              print(no_of_answers)
                              if no_of_answers:
                                   print("no_of_answers:",no_of_answers)
                                   answers = read_answers_azure(new_paper['id'])
                                   if answers:
                                       answers = read_answers_azure(new_paper['id'])
                                       print("answers:::",answers)
                                       answer_images = get_images(os.path.join('../data/answers/', new_paper['id']))
                                       urls = []
                                       
                                       for i, image in enumerate(answer_images):
                                            with open(image, "rb") as files:
                                                 upload = UploadFile(filename=image, file=files)
                                                 filename = f"Q_{i+1}"
                                                 file_url = await upload_file2(upload, "uploads/images/answers/papers", new_paper['id'], filename)
                                                 urls.append(file_url)
                                            question_no = answers[i]["question no"]
                                            answer_text = answers[i]["text"]
                                            print("user_id:",new_paper['paper'].split(".")[0])
                                            answer = AnswerCreate(
                                                 paperNo=new_paper['id'], 
                                                 subjectId= new_paper['subjectId'], 
                                                 userId=new_paper['paper'].split(".")[0], 
                                                 questionNo=question_no, 
                                                 text=answer_text,
                                                 uploadUrl= file_url,
                                                 accuracy=0.0,
                                                 keywordsaccuracy=0.0,
                                                 marks= 0.0
                                            )
                                            answer_id = answer_model.save_answer(request, answer)
                                            print("answer_id:",answer_id)
                                       papers_created.append(new_paper)
                                       print("papers_created:",papers_created)

                                   else:
                                        return JSONResponse({
                                             "message": "error getting answers"
                                             },
                                             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                        )
                              else:
                                   return JSONResponse({
                                        "message": "couldn't extract answers"
                                        },
                                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                   )
                         except OSError:
                              return {"error": OSError}
                    else:
                         raise HTTPException(
                              status_code=status.HTTP_404_NOT_FOUND, 
                              detail="Error in file upload"
                         )

               if papers_created:
                    return JSONResponse({
                         "detail": "New papers added", 
                         "data": [paper["id"] for paper in papers_created],
                         "indexNos": [paper['paper'].split(".")[0] for paper in papers_created]
                    }, 
                    status_code=status.HTTP_200_OK
                    )

               raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Error in file upload"
               )

     else:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Add subject First"
          )
          
# @router.post('/upload/file/', response_description="Add new papers", response_model=List[Paper], status_code=status.HTTP_201_CREATED)
# async def upload_files(request: Request, files: List[UploadFile] = File(...), year: str = Form(...), subjectId: str = Form(...)):          
@router.post('/upload/marks_type',response_description="Add assignment marks", response_model=List[Paper], status_code=status.HTTP_201_CREATED)
async def upload_marks(request: Request, files: List[UploadFile] = File(...), marks_type: str = Form(...), year: str = Form(...), subjectId: str = Form(...)):
     
     # Get the subjectCode and subjectName using subjectId
     subject = subject_model.subject_by_id(request, subjectId)
     print("This is subject",subject)
     # Check if the uploaded file is a CSV file
     if files.filename.endswith('.csv'):
        # Read the content of the CSV file
        contents = await files.read()
        contents_str = contents.decode('utf-8')  # Assuming the file is UTF-8 encoded
        
        # Split the CSV content by lines
        lines = contents_str.split('\n')
        
        lineOne = lines[0].split(',')
        # print("This is line one",lineOne)
        fullMarksList = []
        fullMarksForSubjectCollection = []
        
        # Skip the first line (header) and process the rest
        for line in lines[1:]:
          # Process the CSV data line by line here
          # print("This is line :",line)
            
          marksList = line.split(',')
          marksDict = { }
          marksDictForSubjectCollection = {}
          if(len(marksList)>0):
               # print("This is marks list",marksList)
               
               for index, value in enumerate(marksList): 
                    marksDict.update({lineOne[index]:value})
                    
                    # After 0 index ther values will be index and marks
                    if(index>0):
                         marksDictForSubjectCollection.update({lineOne[index]:value})
                    
          
          fullMarksList.append(marksDict) 
          
          fullMarksForSubjectCollection.append(marksDictForSubjectCollection)
          
          if(marks_type=="assignmentMarks"):
               filters = {"_id":ObjectId(subject['id'])} 
               data = {"finalAssignmentMarks":fullMarksForSubjectCollection}
               subject_model.update(request,filters, data)
          else:
               pass
          
          
          # Now csv file is generalised and stored in fullMarksList, now add that data into student_subject collection
          for studentMarks in fullMarksList:
               
               # check if user details alredy in the student_subject collection
               index = studentMarks['index']
               student_subject = student_subject_model.by_index(request, index)
               # print("This is student subject", student_subject)
               
               if student_subject:
                    subjectListOfStudent = student_subject['subject']
                    
                    # get the subject by subject
                    for subjectOfStudent in subjectListOfStudent:
                         if subjectOfStudent['subject_code'] == subject['subjectCode']:
                              # update the marks
                              subjectOfStudent.update({marks_type: studentMarks[marks_type]})
                              # print("this is subjectOfStudent",subjectOfStudent)
                              
                              # update the exixting
                              filters = {"index":index} 
                              data = {"subject":subjectListOfStudent}
                              student_subject_update = student_subject_model.update(request, filters, data)
                              # print("this is result after update", student_subject_update);    
               else:
                    # create new student_subject collection
                    # print("This is student subject else close")
                    new_student_subject = add_student_subject(request,subject,index)
                    # print("this is end of else", new_student_subject)
                       

          data = {
                 "status": 200,
                 "message": "File uploaded successfully",
                 "marks":fullMarksList,
                 "marksForSubjectCollection":fullMarksForSubjectCollection
             }
     return data
