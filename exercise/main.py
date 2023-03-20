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
    return "Welcome to User Application. Built with FastAPI and. "

@app.post("/user/create", response_model=schemas.userall, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.usercreate, session: Session = Depends(get_session)):

    # create an instance of user Model
    user_obj = models.user(email=user.email,
    password=user.password,
    phone=user.phone,
    city=user.city,
    state=user.state,
    country=user.country,
    status=user.status)

    # Add the object into our database Table
    session.add(user_obj)
    session.commit()
    session.refresh(user_obj)

    # return the user object
    return user_obj

@app.get("/fetch_all_users", response_model = List[schemas.userall])
def read_todo_list(session: Session = Depends(get_session)):
    # get all todo items    
    user_list = session.query(models.user).all()
    return user_list
    
@app.get("/fetch_user_by_id/{id}", response_model=schemas.userall)
def read_todo_id(id: int, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table    
    user_obj = session.query(models.user).get(id)
    # Check if there is record with the provided id, if not then Raise 404 Exception    
    if not user_obj:
        raise HTTPException(status_code=404, detail=f"user item with id {id} not found")
    return user_obj 

@app.put("/user/update_user_by_id/{id}", response_model=schemas.userall)
def update_user(id: int, email: str, password:str, phone:str, session: Session = Depends(get_session)):

    # Fetch user record using id from the table
    user_obj = session.query(models.user).get(id)

    # If the record is present in our DB table then update 
    if user_obj:
        user_obj.email = email
        user_obj.password = password
        user_obj.phone = phone

    # if user item with given id does not exists, raise exception and return 404 not found response
    if not user_obj:
        raise HTTPException(status_code=404, detail=f"user item with id {id} not found")

    return user_obj

@app.delete("/user/delete_user_by_id/{id}", response_model = str)
def delete_user(id: int, session: Session = Depends(get_session)):

    # Fetch user record using id from the table
    user_obj = session.query(models.user).get(id)

    # Check if user record is present in our Database,If not then raise 404 error
    if user_obj:
        session.delete(user_obj)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"user item with id {id} not found")

    return f"user task with id {id} successfully deleted"