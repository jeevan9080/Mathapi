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
    return "Welcome to tax Application. Built with FastAPI."

@app.post("/create", response_model=schemas.taxall, status_code=status.HTTP_201_CREATED)
def create_tax(tax: schemas.taxcreate, session: Session = Depends(get_session)):

    # create an instance of tax Model
    tax_obj = models.tax(id=tax.id,
    name=tax.name)

    # Add the object into our database Table
    session.add(tax_obj)
    session.commit()
    session.refresh(tax_obj)

    # return the tax object
    return tax_obj

@app.get("/setup", response_model = List[schemas.taxall])
def read_todo_list(session: Session = Depends(get_session)):
    # get all todo items    
    tax_list = session.query(models.tax).all()
    return tax_list
    
@app.get("/read/id{id}", response_model=schemas.taxall)
def read_todo_id(id: str, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table    
    tax_obj = session.query(models.tax).get(id)
    # Check if there is record with the provided id, if not then Raise 404 Exception    
    if not tax_obj:
        raise HTTPException(status_code=404, detail=f"tax item with id {id} not found")
    return tax_obj 

@app.put("/update/id{id}", response_model=schemas.taxall)
def update_tax(id: str, name: str, session: Session = Depends(get_session)):

    # Fetch tax record using id from the table
    tax_obj = session.query(models.tax).get(id)

    # If the record is present in our DB table then update 
    if tax_obj:
        tax_obj.id = id
        tax_obj.name = name

    # if tax item with given id does not exists, raise exception and return 404 not found response
    if not tax_obj:
        raise HTTPException(status_code=404, detail=f"tax item with id {id} not found")

    return tax_obj

@app.delete("/delete/id{id}", response_model = str)
def delete_tax(id: str, session: Session = Depends(get_session)):

    # Fetch tax record using id from the table
    tax_obj = session.query(models.tax).get(id)

    # Check if tax record is present in our Database,If not then raise 404 error
    if tax_obj:
        session.delete(tax_obj)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"tax item with id {id} not found")

    return f"tax record with id {id} successfully deleted"