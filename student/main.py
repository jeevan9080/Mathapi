from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, Request
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import models

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# provides database session to each request upon calling
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "Welcome to student Application. Built with FastAPI."

@app.post("/create/ ", response_model=schemas.studentall, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.studentcreate, session: Session = Depends(get_session)):

    # create an instance of student Model
    student_obj = models.student(name=student.name)

    # Add the object into our database Table
    session.add(student_obj)
    session.commit()
    session.refresh(student_obj)

    # return the student object
    return student_obj

@app.get("/setup", response_model = List[schemas.studentall])
def read_todo_list(session: Session = Depends(get_session)):
    # get all todo items    
    student_list = session.query(models.student).all()
    return student_list
    
@app.get("/read/id{id}", response_model=schemas.studentall)
def read_todo_id(id: str, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table    
    student_obj = session.query(models.student).get(id)
    # Check if there is record with the provided id, if not then Raise 404 Exception    
    if not student_obj:
        raise HTTPException(status_code=404, detail=f"student item with id {id} not found")
    return student_obj 

@app.put("/update/id{id}", response_model=schemas.studentall)
def update_student(id: str, name: str, session: Session = Depends(get_session)):

    # Fetch student record using id from the table
    student_obj = session.query(models.student).get(id)

    # If the record is present in our DB table then update 
    if student_obj:
        student_obj.id = id
        student_obj.name = name

    # if student item with given id does not exists, raise exception and return 404 not found response
    if not student_obj:
        raise HTTPException(status_code=404, detail=f"student item with id {id} not found")

    return student_obj

@app.delete("/delete/id{id}", response_model = str)
def delete_student(id: str, session: Session = Depends(get_session)):

    # Fetch student record using id from the table
    student_obj = session.query(models.student).get(id)

    # Check if student record is present in our Database,If not then raise 404 error
    if student_obj:
        session.delete(student_obj)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"student item with id {id} not found")

    return f"student record with id {id} successfully deleted"