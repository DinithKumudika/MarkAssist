from fastapi import APIRouter, HTTPException, status, Request,Depends,UploadFile, File,Form
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from bson.objectid import ObjectId

from models.marking_scheme import MarkingSchemeModel
from schemas.marking_scheme import MarkingScheme,MarkingSchemeCreate,MarkingSchemeForm

from models.subject import SubjectModel;

from schemas.user import User
from utils.auth import get_current_active_user

from utils.firebase_storage import upload_file 

router = APIRouter()
marking_scheme_model = MarkingSchemeModel()
subject_model = SubjectModel()

@router.get("/", response_description="Get all marking schemes",response_model=List[MarkingScheme])
async def get_All(request: Request):
     # print("This is user",current_user)
     markings = marking_scheme_model.list_marking_schemes(request)
     if markings:
          return markings 
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, 
          detail="No marking schems to show"
     )
     
@router.post("/", response_description="Add a marking scheme", response_model = MarkingScheme, status_code= status.HTTP_201_CREATED)
async def add_marking(request: Request, file: UploadFile = File(...), year: str = Form(...), subjectId: str = Form(...) ):
    
    # get the subjectCode and subjectName using subjectId
    subject = subject_model.subject_by_id(request, subjectId);
    if(subject):
        # print("There is subject")
        # print(subject['subjectName'])
        # print(subject['subjectCode'])
        # print(file.filename)

        # Upload the file and get the file URL
        marking_url = await upload_file(file,file.filename)  # Assuming you have implemented the `upload_file` function

        # Create a new MarkingScheme object with the provided data and file URL
        marking_scheme = MarkingSchemeCreate(
            subjectCode=subject['subjectCode'],
            subjectName=subject['subjectName'],
            year=year,
            subjectId=str(subjectId),
            markingUrl=marking_url,
        )
        
        # print(jsonable_encoder(marking_scheme));

        # Save the marking scheme to the database using your model
        new_marking_scheme = await marking_scheme_model.add_new_marking(request, marking_scheme)
        if new_marking_scheme:
            return new_marking_scheme

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No marking schemes to show"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Add subject First"
        )
    

@router.put('/update', response_description="Update an existing marking scheme")
async def update_marking(request:Request,file: UploadFile = File(...),subjectCode: str = Form(...),year: int = Form(...),subjectId: str = Form(...)):
     pass


# @router.get("/{marking_id}", response_description="Get a marking scheme id")
# async def get_by_id(marking_id):
#      pass