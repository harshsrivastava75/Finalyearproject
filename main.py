from fastapi import FastAPI

from app.database import Base, engine

from app.models import User
from app.models import Student
from app.models import Attendance
from app.models import FaceEmbedding

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Facial Attendance Tracker Backend"
    }