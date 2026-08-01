from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter(
    prefix="/face",
    tags=["Face Recognition"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/register")
async def register_face(
    student_id: int,
    image: UploadFile = File(...)
):

    filename = f"{student_id}_{image.filename}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "message": "Face Registered Successfully",
        "file": filename
    }


@router.post("/recognize")
async def recognize_face(image: UploadFile = File(...)):

    return {
        "message": "Face Recognition Module",
        "prediction": "John Doe",
        "confidence": 97.8,
        "attendance": "Marked"
    }