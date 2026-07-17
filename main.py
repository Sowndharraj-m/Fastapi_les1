from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    department: str


# Temporary Database
students = []


# Create
@app.post("/students")
def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    students.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }


# Read All
@app.get("/students")
def get_students():
    return students


# Read One
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


# Update
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(status_code=404, detail="Student not found")


# Delete
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")