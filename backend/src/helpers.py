from fastapi import Request
from typing import Optional, List
import time
import pdf2image as p2i
import cv2
import numpy as np
import openai
import screeninfo
from google.cloud import vision
import pandas as pd
import pytesseract
import nltk
import textdistance
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from thefuzz import process
# from thefuzz import fuzz
from fuzzywuzzy import fuzz
from itertools import product
from pytesseract import Output
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

from models.paper import PaperCreate

from models.student_subject import StudentSubjectModel
from schemas.student_subject import StudentSubjectCreate



import os
import io

from config.config import settings

student_subject_model = StudentSubjectModel()


# Download NLTK resources if not already downloaded
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')


def get_screen_width():
     screen = screeninfo.get_monitors()[0]
     return screen.width


def get_screen_height():
     screen = screeninfo.get_monitors()[0]
     return screen.height


# convert pdf pages to images
def convert_to_images(file, path):
     pages = p2i.convert_from_path(file, 500)
     count = 1
     images = [] 
     for i, page in enumerate(pages):
          image = path + '/img-' + str(count) + ".jpg"
          count += 1
          page.save(image, "JPEG")
          images.append(image)
     
     return images


# get images already saved inside data/images
def get_images(dir_path):
     images_arr = []
     for image in os.listdir(dir_path):
          if(image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg")):
               images_arr.append(dir_path + '/' + image)
     return images_arr


# resize an image
def resize(image, screen_height, screen_width):
     height = screen_height
     width = int(screen_width / 2)
     dimensions = (width, height)
     return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)


# detect contours in image
def detect_edges(image):
     grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     blurred_image = cv2.GaussianBlur(grayscale_image, (5,5), cv2.BORDER_DEFAULT)
     
     # edge cascade
     t_lower = 130   #lower threshold
     t_upper = 225   #upper threshold
     edged_image = cv2.Canny(image=blurred_image, threshold1=t_lower, threshold2=t_upper, L2gradient=True)
     dilated_image = cv2.dilate(edged_image,(5,5), iterations=1)

     contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
     return contours


def draw_rectangle(event, x, y, flags, param):
     global is_selecting
     selection = []
     
     if event == cv2.EVENT_LBUTTONDOWN:
          print(f"mouse down (x={x}, y={y})")
          param["coords"].append([(x, y)])     
          is_selecting = True
     elif event == cv2.EVENT_LBUTTONUP:
          print(f"mouse up (x={x}, y={y})")
          
          # get array in last index and append
          param["coords"][-1].append((x, y))
          is_selecting = False
          
          # draws a rectangle on the image using the coordinates of the last selected area stored in selection
          cv2.rectangle(param["image"], param["coords"][-1][0], param["coords"][-1][1], (0, 255, 0), 2)
          cv2.imshow("Mark answer", param["image"])


def save_image(image, path, crop_index, image_index):
     cv2.imwrite(f"{path}/cropped_{str(image_index + 1)}-{str(crop_index + 1)}.jpg", image)

def crop_and_save(image, coords, path, crop_index, image_index):
     x_start, y_start = coords[0]
     x_end, y_end = coords[1]
     cropped_image = image[y_start:y_end, x_start:x_end]
     cv2.imwrite(f"{path}/cropped_{str(image_index + 1)}-{str(crop_index + 1)}.jpg", cropped_image)
     print(f'Cropped image {str(image_index + 1)}-{str(crop_index + 1)} saved.')
     
     
def read_text(client, image):
     with io.open(image, "rb") as image_file:
          content = image_file.read()
     image = vision.Image(content=content)
     response = client.document_text_detection(image=image)
     text = response.full_text_annotation.text
     return text


def read_text_azure(client : ComputerVisionClient, image):
     response = client.read_in_stream(open(image, 'rb'), language='en', raw=True)
     operation_location = response.headers["Operation-Location"]
     operation_id = operation_location.split("/")[-1]
     time.sleep(5)
     result = client.get_read_result(operation_id)
     text_lines = []
     

     if result.status == OperationStatusCodes.succeeded:
          read_results = result.analyze_result.read_results
          for analyzed_results in read_results:
               for line in analyzed_results.lines:
                    print(line.text)
                    text_lines.append(line.text)
     
     return text_lines


def show_text(image, options):
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
     data = pytesseract.image_to_data(gray, config = options, output_type=Output.DICT)
     n_boxes = len(data['text'])
     
     for i in range(n_boxes):
          if float(data['conf'][i]) > 60:
               (x, y , w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
               cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
               print(data['text'][i])
               
     cv2.imshow("question no", image)
     cv2.waitKey(0)
     

def text_similarity(text1: str, text2: str)->str:
     openai.api_key = settings.OPENAI_API_KEY
     # Prepare the prompt
     prompt = f"""Text 1: {text1}\nText 2: {text2}\n
               You are a marker who mark exam papers by comparing student answer and marking scheme answer. 
               Text 1 is the answer of the marking scheme and Text 2 is the answer written by the student for a question.
               Compare both Text 1 and Text 2 using both cosine similarity and semantic analysis techniques together with the context. 
               then provide me a score as a percentage between 0 and 1 in below format. Overall score is: score after comparison"""

     # Make an API request
     response = openai.Completion.create(
          engine='text-davinci-003',
          prompt=prompt,
          max_tokens=256,
          n=1,
          stop=None,
          temperature=0,
     )

     # Retrieve and process the response
     completion_text = response['choices'][0]['text'].strip()
     return completion_text

def preprocess_text(text):
    # Tokenize the text and convert to lowercase
    words = word_tokenize(text.lower())
    
    # Remove punctuation and stop words
    words = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return words

def find_keywords_in_text(text, keywords):
    processed_text = preprocess_text(text)
    keyword_matches = []
    
    for keyword in keywords:
        singular_form = WordNetLemmatizer().lemmatize(keyword, 'n')
        plural_form = WordNetLemmatizer().lemmatize(keyword + 's', 'n')
        
        if singular_form in processed_text or plural_form in processed_text:
            keyword_matches.append(keyword)
        else:
            # Check for keywords with spelling mistakes
            for word in processed_text:
                if textdistance.hamming.normalized_distance(keyword, word) <= 0.4:
                    keyword_matches.append(keyword)
                    break
    
    return keyword_matches

def keywords_match(paragraph: str, keywords: list):
     matching_keywords = find_keywords_in_text(paragraph, keywords)
     
     if matching_keywords:
         print("Keywords found:", matching_keywords)
         return len(matching_keywords)
     else:
         print("No keywords found.")
         return 0

# def keyword_accuracy(answer_student: str, keywords: list):
#      keywordsAccuracy=0
#      # keywordsAccuracy
#      collection = ["AFC Barcelona", "Barcelona AFC", "barcelona fc", "afc barcalona"]
#      print(process.extract(answer_student["text"], keywords, scorer=fuzz.ratio))
#      # print(f"Partial ratio similarity score: {fuzz.partial_ratio(keywords[0], answer_student['text'])}")
#      # But order will not effect simple ratio if strings do not match
#      for keyword in keywords:
#           print(f"Partial ratio similarity score {keyword.lower()} => [{answer_student['text'].lower()}]: {fuzz.partial_ratio(keyword.lower(), answer_student['text'].lower())}")
#           if fuzz.ratio(keyword, answer_student['text']) > 50:
#                keywordsAccuracy+=100/len(keywords)
#      print(f"Simple ratio similarity score: {fuzz.ratio(keywords[0], answer_student['text'])}")
#      result_string = ' '.join(keywords)
#      no_keywords= len(keywords)
#      print("no_keywords",no_keywords)
#      keywords=[]
#      for keyword in keywords:
#           print("keyword",keyword)
#           if keyword.lower() in answer_student["text"].lower():
#               print(f"'{keyword}' is present in the paragraph.")
#               if keyword in keywords:
#                    print(keywords)
#                #     pass
#               else:
#                    print("Keywords::",keywords)
#                    keywords.append(keyword)
#                    keywordsAccuracy+=100/no_keywords
#           else:
#               print(f"'{keyword}' is not present in the paragraph.")
#      print("keywordsAccuracy",keywordsAccuracy)

def check_keywords_in_paragraph(paragraph, keywords, threshold=80):
    # Initialize a dictionary to store keyword matches
    keyword_matches = {keyword: [] for keyword in keywords}
    print("This is check_keywords_in_paragraph function::",paragraph)
    print("This is check_keywords_in_paragraph function::",keywords)

    # Split the paragraph into words
    paragraph_words = paragraph.split()

    for keyword in keywords:
        keyword_words = keyword.split()
        keyword_variations = [' '.join(perm) for perm in product(*[word.split() for word in keyword_words])]
        print("This is keyword_variations",keyword_variations)
        
        for variation in keyword_variations:
            print("This is variation",variation)
            for word in paragraph_words:
                print("This is word",word)
                similarity = fuzz.ratio(variation.lower(), word.lower())
                print(f"Similarity score {variation.lower()} => [{word.lower()}]: {similarity}")
                if similarity >= threshold:
                    keyword_matches[keyword].append(word)

    return keyword_matches

# add new document to student_subject collection 
def add_student_subject(request: Request, subject: dict, index: str):
     # print("This is add student_subject function")
     subject_list = [          
          {
               "subject_id": subject["id"],
               "subject_code": subject["subjectCode"],
               "no_of_credit": subject["no_credits"],
               "academicYear": subject["academicYear"],
               "semester": subject["semester"],
               "assignment_marks": 0,
               "ocr_marks": 0.0,
               "non_ocr_marks": 0.0,
               "total_marks":0.0,
          }
     ]
                    
     student_subject = StudentSubjectCreate(
          index = index,
          gpa = 0.0,
          rank= 0,
          total_credit= 0,
          subject = subject_list
     )
     new_student_subject = student_subject_model.add_new_student_subject(request,student_subject)
     return new_student_subject

# add subject to student_subject collection's document
def add_subject(request: Request,student_subject:dict, subject: dict, index: str):
     #loop the subject list
     print("This is student subject if close")
     
     new_subject_list = []
     for item in student_subject['subject']:
          # find if subject is in the schema
          if item['subject_code'] == subject["subjectCode"] :
               # if subject is alredy in the collection update it
               pass
          else:
               # append the subject to list
               new_subject = {
                    "subject_id": subject["id"],
                    "subject_code": subject["subjectCode"],
                    "no_of_credit": subject["no_credits"],
                    "academicYear": subject["academicYear"],
                    "semester": subject["semester"],
                    "assignment_marks": 0,
                    "ocr_marks": 0.0,
                    "non_ocr_marks": 0.0,
                    "total_marks":0.0,
               }
               # print("is new subject", new_subject);
               # print("this is current list", student_subject["subject"]);
               
               new_subject_list = student_subject['subject'];
               new_subject_list.append(new_subject)
     
          # update the exixting
          filters = {"index":index} 
          data = {"subject":new_subject_list}
          student_subject_update = student_subject_model.update(request, filters, data)
          print("this is result after update", student_subject_update);
                    

# update student_subject collection's document
def update_student_subject_collection(request: Request, subject: dict, index: str,marks_type:str,studentMarks:dict,subjectListOfStudent:List[dict]):
     # get the subject by subject
     # print("This function calls update_student_subject_collection")
     for subjectOfStudent in subjectListOfStudent:
          if subjectOfStudent['subject_code'] == subject['subjectCode']:
               if(marks_type=="assignmentMarks"):
                    # update the marks
                    subjectOfStudent.update({"assignment_marks": studentMarks['assignment_marks']})
                    # print("this is subjectOfStudent",subjectOfStudent)
                    
                    # update the exixting
                    filters = {"index":index} 
                    data = {"subject":subjectListOfStudent}
                    student_subject_update = student_subject_model.update(request, filters, data)
                    # print("this is result after update", student_subject_update);
               else:
                    # This is for nonOCR marks
                    # update the marks
                    subjectOfStudent.update({"non_ocr_marks": studentMarks['non_ocr_marks']})
                    # print("this is subjectOfStudent",subjectOfStudent)
                    
                    # update the exixting
                    filters = {"index":index} 
                    data = {"subject":subjectListOfStudent}
                    student_subject_update = student_subject_model.update(request, filters, data)
                    # print("this is result after update", student_subject_update);
    
    