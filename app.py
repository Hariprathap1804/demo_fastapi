from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from students import (
    students,
    get_all_students,
    get_student_by_id,
    calculate_student_status
)

app = FastAPI(
    title="Student Performance API",
    description="API for managing student performance with standard HTTP status codes",
    version="1.0.0"
)

class Student(BaseModel):
    id: int
    name: str
    course: str
    attendance: float
    marks: float


@app.get("/")
def home():
    return {"message": "Student Performance API is running"}


@app.get("/students")
def get_students():
    return get_all_students()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    return student



@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_student(student: Student):
    if get_student_by_id(student.id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Student with ID {student.id} already exists"
        )

    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    students.remove(student)
    return None