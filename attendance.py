from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

attendance_records = []


@router.post("/mark")
def mark_attendance(student_id: int):

    record = {
        "student_id": student_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "status": "Present"
    }

    attendance_records.append(record)

    return {
        "message": "Attendance Marked",
        "record": record
    }


@router.get("/")
def get_attendance():
    return attendance_records


@router.get("/today")
def today_attendance():

    today = datetime.now().strftime("%Y-%m-%d")

    return [
        record
        for record in attendance_records
        if record["date"] == today
    ]