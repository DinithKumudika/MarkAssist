from typing import List
from fastapi import APIRouter, HTTPException, Request, status, UploadFile
from fastapi.responses import JSONResponse
from fastapi.params import Body
from thefuzz import process
from thefuzz import fuzz
import os

from schemas.answer import AnswerCreate, Answer
from models.answer import AnswerModel, extract_answers, read_answers
from models.marking import MarkingModel
from models.marking_scheme import MarkingSchemeModel
from models.paper import PaperModel
from models.subject import SubjectModel
from models.user import UserModel
from models.student_subject import StudentSubjectModel
from models.grade import GradeModel
from helpers import check_keywords_in_paragraph, get_images, text_similarity, keywords_match,update_student_subject_collection_given_field
from utils.firebase_storage import upload_file2

router = APIRouter()
answer_model = AnswerModel()
marking_model = MarkingModel()
marking_scheme_model = MarkingSchemeModel()
paper_model = PaperModel()
subject_model = SubjectModel()
user_model = UserModel()
student_subject_model = StudentSubjectModel()
grade_model = GradeModel()


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
               accuracy=0.0,
               keywordsaccuracy=0.0,
               marks= 0.0
          )
          answer_id = answer_model.save_answer(request, answer)
          
     return JSONResponse({
               "detail": "answers saved",
               "data": urls
          }, 
          status_code=status.HTTP_201_CREATED
     )

@router.patch('/compare/{markingSchemeId}/{subjectId}', response_description="compare between question text and marking scheme then returns similarity")
async def check_similarity(request: Request, markingSchemeId:str, subjectId: str,  payload: dict = Body(...)):
     # print("marking scheme id", markingSchemeId)
     # # print("student id", stu)
     # print("sub id", subjectId)
     # print("payload", payload)


     markings_by_scheme_id = marking_model.get_by_marking_scheme(request, markingSchemeId)
     # sorting marking scheme answers by question no's
     markings_by_scheme_id = sorted(markings_by_scheme_id, key=lambda x:int(x["questionNo"]))
     # print("no of marking answers", markings_by_scheme_id)

     #loop payload
     for key, value in payload.items():
          studentIndex = key.split('.')[0]
          # print("Student::",studentIndex)
          if(value):

               answers_by_student = answer_model.get_by_subject_student(request, studentIndex, subjectId)
               # sorting student answers by question no's
               answers_by_student = sorted(answers_by_student, key=lambda x:int(x["questionNo"]))

               # print("no of student answers",len(answers_by_student))

               percentages = []
               for i, el in enumerate(answers_by_student):
                    keywordsAccuracy=0
                    # print("student answer", i+1, ":", answers_by_student[i]["text"])
                    # print("Marking answer", i+1, ":", markings_by_scheme_id[i]["text"])

                    if(markings_by_scheme_id[i]["selected"]):
                         percentage = text_similarity(markings_by_scheme_id[i]["text"], answers_by_student[i]["text"])
                         # print("Percentage:",percentage)

                         # no_of_matched_keywords = keywords_match(answers_by_student[i]["text"],markings_by_scheme_id[i]["keywords"])

                         # Sample paragraph and keywords
                         paragraph = "This is an example paragraf with some misspelled words."
                         keywords = ["paragraph", "example", "spelling mistakes", "some words"]
                         
                         # Set a similarity threshold (adjust as needed)
                         threshold = 80
                         
                         # Check for keywords in the paragraph
                         matches = check_keywords_in_paragraph(answers_by_student[i]["text"], markings_by_scheme_id[i]["keywords"], threshold)
                         print("matches::",matches)
                         # Print the matches
                         keywords_accuracy = 0
                         no_of_matched_keywords = 0
                         for keyword, matched_words in matches.items():
                             if matched_words:
                                 no_of_matched_keywords+=1
                         #     else:
                              #    print(f"Keyword '{keyword}' not found in the paragraph.")
                         # keywords_accuracy = (keywords_accuracy/len(markings_by_scheme_id[i]["keywords"]))*100
                         print("no_of_matched_keywords",no_of_matched_keywords)
                         no_of_keywords = len(markings_by_scheme_id[i]["keywords"])
                         # print("no_of_keywords",no_of_keywords)
                         if(no_of_keywords != 0):
                              keywordsAccuracy = (no_of_matched_keywords/no_of_keywords)*100
                         elif (no_of_keywords == 0):
                              keywordsAccuracy = 0
                         elif (no_of_matched_keywords == 0):
                              keywordsAccuracy = 0
                         print("keywordsAccuracy",keywordsAccuracy)

                         # here we should by questionNo,userId,subjectId
                         filters = {"userId":studentIndex, "questionNo":str(i+1), "subjectId":subjectId}
                         data = {"accuracy":percentage.split(": ")[-1], "keywordsaccuracy":keywordsAccuracy}
                         # data = {"accuracy":"0.6"}
                         # print("filters", data)

                         answer_model.update(request, filters , data)
                
               
                         percentages.append({
                              "subjectId":subjectId,
                              "userId":studentIndex,
                              "questionNoquestion": i+1, 
                              "accuracy": percentage.split(": ")[-1],
                              "keywordsaccuracy":keywordsAccuracy
                              # "accuracy": "0.6"
                         })
               # # print("key:::::::::", key)
               paper_filters = {"paper":key,"subjectId":subjectId}
               paper_data = {"marksGenerated":True}
               paper_model.update(request, paper_filters, paper_data)          
               
     return JSONResponse({
               # "similarity percentages": percentages
          },
          status_code=status.HTTP_200_OK
     )
               # # keywordsAccuracy
               # collection = ["AFC Barcelona", "Barcelona AFC", "barcelona fc", "afc barcalona"]
               # print(process.extract(answers_by_student[i]["text"], markings_by_scheme_id[i]['keywords'], scorer=fuzz.ratio))
          #      # print(f"Partial ratio similarity score: {fuzz.partial_ratio(markings_by_scheme_id[i]['keywords'][0], answers_by_student[i]['text'])}")
          #     # But order will not effect simple ratio if strings do not match
          #      for keyword in markings_by_scheme_id[i]["keywords"]:
          #           print(f"Partial ratio similarity score {keyword.lower()} => [{answers_by_student[i]['text'].lower()}]: {fuzz.partial_ratio(keyword.lower(), answers_by_student[i]['text'].lower())}")
                    # if fuzz.ratio(keyword, answers_by_student[i]['text']) > 50:
                    #      keywordsAccuracy+=100/len(markings_by_scheme_id[i]['keywords'])
               # print(f"Simple ratio similarity score: {fuzz.ratio(markings_by_scheme_id[i]['keywords'][0], answers_by_student[i]['text'])}")


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
               # print("keywordsAccuracy",keywordsAccuracy)
               
               
     
     

#*****************Wada karana eka*****************
# @router.get('/compare/{markingSchemeId}', response_description="compare between question text and marking scheme then returns similarity")
# async def check_similarity(request: Request, markingSchemeId:str, sub: str, stu: str):
#      print("marking scheme id", markingSchemeId)
#      print("student id", stu)
#      print("sub id", sub)
#      # print("payload", payload)
#      answers_by_student = answer_model.get_by_subject_student(request, stu, sub)
#      # sorting student answers by question no's
#      answers_by_student = sorted(answers_by_student, key=lambda x:int(x["questionNo"]))
     
#      markings_by_scheme_id = marking_model.get_by_marking_scheme(request, markingSchemeId)
#      # sorting marking scheme answers by question no's
#      markings_by_scheme_id = sorted(markings_by_scheme_id, key=lambda x:int(x["questionNo"]))
     
#      # print("no of student answers",answers_by_student)
#      # print("no of marking answers", markings_by_scheme_id)
     
#      percentages = []
#      for i, el in enumerate(answers_by_student):
#           keywordsAccuracy=0
#           # print("student answer", i+1, ":", answers_by_student[i]["text"])
#           # print("Marking answer", i+1, ":", markings_by_scheme_id[i]["text"])

#           if(markings_by_scheme_id[i]["selected"]):
#                # percentage = text_similarity(markings_by_scheme_id[i]["text"], answers_by_student[i]["text"])
#                # print("Percentage:",percentage)
               
#                # # here we should by questionNo,userId,subjectId
#                # filters = {"userId":stu, "questionNo":str(i+1), "subjectId":sub}
#                # data = {"accuracy":percentage.split(": ")[-1]}
#                # # data = {"accuracy":"0.6"}
#                # print("filters", data)

#                # # keywordsAccuracy
#                # collection = ["AFC Barcelona", "Barcelona AFC", "barcelona fc", "afc barcalona"]
#                print(process.extract(answers_by_student[i]["text"], markings_by_scheme_id[i]['keywords'], scorer=fuzz.ratio))
#                # print(f"Partial ratio similarity score: {fuzz.partial_ratio(markings_by_scheme_id[i]['keywords'][0], answers_by_student[i]['text'])}")
#               # But order will not effect simple ratio if strings do not match
#                for keyword in markings_by_scheme_id[i]["keywords"]:
#                     print(f"Partial ratio similarity score {keyword.lower()} => [{answers_by_student[i]['text'].lower()}]: {fuzz.partial_ratio(keyword.lower(), answers_by_student[i]['text'].lower())}")
#                     # if fuzz.ratio(keyword, answers_by_student[i]['text']) > 50:
#                     #      keywordsAccuracy+=100/len(markings_by_scheme_id[i]['keywords'])
#                # print(f"Simple ratio similarity score: {fuzz.ratio(markings_by_scheme_id[i]['keywords'][0], answers_by_student[i]['text'])}")


#                # result_string = ' '.join(markings_by_scheme_id[i]["keywords"])
#                # no_keywords= len(markings_by_scheme_id[i]['keywords'])
#                # print("no_keywords",no_keywords)
#                # keywords=[]
#                # for keyword in markings_by_scheme_id[i]["keywords"]:
#                #      print("keyword",keyword)
#                #      if keyword.lower() in answers_by_student[i]["text"].lower():
#                #          print(f"'{keyword}' is present in the paragraph.")
#                #          if keyword in keywords:
#                #               print(keywords)
#                #           #     pass
#                #          else:
#                #               print("Keywords::",keywords)
#                #               keywords.append(keyword)
#                #               keywordsAccuracy+=100/no_keywords
#                #      else:
#                #          print(f"'{keyword}' is not present in the paragraph.")
               
#                # answer_model.update(request, filters , data)
#                # print("keywordsAccuracy",keywordsAccuracy)
                
               
#                # percentages.append({
#                #      "subjectId":sub,
#                #      "userId":stu,
#                #      "questionNoquestion": i+1, 
#                #      "accuracy": percentage.split(": ")[-1]
#                #      # "accuracy": "0.6"
#                # })
#      return JSONResponse({
#                "similarity percentages": percentages
#           },
#           status_code=status.HTTP_200_OK
#      )
     
     
@router.patch('/calculate_marks/{markingSchemeId}/{subjectId}', response_description="calculate marks for a student subject")
async def calculate_marks(request: Request, markingSchemeId:str, subjectId: str,):
     print("you are calling this function calculate_marks")
     
     print("marking scheme id", markingSchemeId)

     print("subject id", subjectId)
     
     # get the marking scheme by marking scheme id
     marking_scheme_by_id = marking_scheme_model.by_id(request, markingSchemeId)
     
     # get the marking of the marking scheme by marking scheme id
     markings_by_scheme_id = marking_model.get_by_marking_scheme(request, markingSchemeId)
     # sorting marking scheme answers by question no's
     markings_by_scheme_id = sorted(markings_by_scheme_id, key=lambda x:int(x["questionNo"]))
     
     # get paper list according to subject id and marksGenerated field value
     papers_list = paper_model.papers_by_subjectId_and_marksGenerated(request, subjectId, True)
     
     if(papers_list):
          userId = ""
          # loop the papers_list
          for paper in papers_list:
               userId = paper['paper'][:-4]; # 20001721.pdf ---> 20001721
               
               answers_by_student = answer_model.get_by_subject_student(request, userId, subjectId)
               # sorting student answers by question no's
               answers_by_student = sorted(answers_by_student, key=lambda x:int(x["questionNo"]))
               
               totalMarksForPaper = 0
               answers = []
               for i, el in enumerate(answers_by_student):
                    # print("student answer", i+1, ":", answers_by_student[i]["text"])
                    # print("Marking answer", i+1, ":", markings_by_scheme_id[i]["text"])

                    if(markings_by_scheme_id[i]["selected"]):
                         print("student answer:::", i+1)
                         marks_reserverd_in_marking = int(markings_by_scheme_id[i]["marks"])
                         keywords_marks_reserverd_in_marking = int(markings_by_scheme_id[i]["keywordsMarks"])
                         markConfig = marking_scheme_by_id["markConfig"]
                         accuracy_percentage = float(answers_by_student[i]["accuracy"])*100
                         keywords_accuracy_percentage = answers_by_student[i]["keywordsaccuracy"]
                         print("accuracy_percentage",accuracy_percentage)
                         print("marks_reserverd_in_marking",marks_reserverd_in_marking)
                         print("markConfig",markConfig)
                         mark_percentage = 0
                         for value in markConfig:
                              print("accuracy_percentage",value['minimum'])
                              
                              if( (value['minimum'] <= accuracy_percentage) and (value['maximum'] >= accuracy_percentage)  ):
                                   mark_percentage = value['percentageOfMarks']
                                   print("mark_percentage",mark_percentage)
                         marks = (marks_reserverd_in_marking * mark_percentage)/100
                         print("Previosmarks::::::",marks)
                         marks += (keywords_marks_reserverd_in_marking * keywords_accuracy_percentage)/100
                         print("Afterrrrrmarks::::::",marks)

                         
                         totalMarksForPaper+=marks
                         
                         # here we should by questionNo,userId,subjectId
                         filters = {"userId":userId, "questionNo":str(i+1), "subjectId":subjectId}
                         data = {"marks":marks}
                         
                         updated_answer =  answer_model.update(request, filters , data)
                         
                         print("filters", data)
                         
                         answers.append({
                              "questionNo": i+1,
                              "marks":marks
                              
                         })
               # get subject by subject id
               subject = subject_model.subject_by_id(request, subjectId)
               # get student subject by student index
               student_subject = student_subject_model.by_index(request, userId)
               # get student subject list
               subjectListOfStudent = student_subject['subject']
               field = ['ocr_marks','total_marks']
               
               # in here user id means index
               for subjectOfStudent in subjectListOfStudent:
                    if subjectOfStudent['subject_code'] == subject['subjectCode']:
                         current_total_mark_of_ocr = float(subjectOfStudent['ocr_marks']) * float(subject['paperMarks']/100)
                         total_mark_of_ocr = float(totalMarksForPaper) * float(subject['paperMarks']/100)
                         total_marks = subjectOfStudent['total_marks'] - current_total_mark_of_ocr + total_mark_of_ocr 
                         # print("DATA1:::::",current_total_mark_of_ocr)
                         # print("DATA3:::::",total_mark_of_ocr)
                         # print("DATA2:::::",total_marks)
                         # print("DATA4:::::",subjectOfStudent['total_marks'])
                         
                         field_value = {'ocr_marks':round(totalMarksForPaper,2),'total_marks':round(total_marks,2)}
                         print("This is total marks",totalMarksForPaper)
                         student_subject_update =  update_student_subject_collection_given_field(request,subjectOfStudent, subject, userId, subjectListOfStudent,field,field_value)
                         print("student subject update:::",student_subject_update)
                         
                         updated_subjectListOfStudent = student_subject_update['subject']
                         for updated_subjectOfStudent in updated_subjectListOfStudent:
                              if updated_subjectOfStudent['subject_code'] == subject['subjectCode']:
                                   grade = grade_model.grade_and_gpv(request, updated_subjectOfStudent['total_marks'])
                                   update_student_subject_collection_given_field(request,subjectOfStudent, subject, userId, subjectListOfStudent,{'grade'},{'grade':grade['grade']})
                                   update_student_subject_collection_given_field(request,subjectOfStudent, subject, userId, subjectListOfStudent,{"gpv"},{"gpv":grade['gpv']})
                         
          return JSONResponse({
                    "similarity percentages": "ok"
               },
               status_code=status.HTTP_200_OK
          )
               
     else:  
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND, 
               detail=f"No papers related to subject id {subjectId}"
          )
          
     
     