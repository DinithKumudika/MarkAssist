import pdf2image as p2i
import cv2
import numpy as np
import openai
import screeninfo
from google.cloud import vision
import pandas as pd
import pytesseract
from pytesseract import Output

import os
import io

from config.config import settings

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