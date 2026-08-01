from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

students = []

@router.get("/")
def get_students():
    return students


@router.post("/")
def add_student(student: dict):
    students.append(student)
    return {
        "message": "Student Added Successfully",
        "student": student
    }


@router.get("/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student Not Found")


@router.put("/{student_id}")
def update_student(student_id: int, updated: dict):

    for index, student in enumerate(students):

        if student["id"] == student_id:
            students[index] = updated
            return {
                "message": "Student Updated",
                "student": updated
            }

    raise HTTPException(status_code=404, detail="Student Not Found")


@router.delete("/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student Deleted"
            }

    raise HTTPException(status_code=404, detail="Student Not Found")