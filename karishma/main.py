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
    return "Welcome to tax Calculation. Built with FastAPI."

@app.post("/create", response_model=schemas.taxall, status_code=status.HTTP_201_CREATED)
def create_tax(tax: schemas.taxcreate, session: Session = Depends(get_session)):

    # create an instance of tax Model
    tax_obj = models.tax(Name=tax.Name,
    Description=tax.Description,
    Price=tax.Price,
    GST=tax.GST)

    # Add the object into our database Table
    session.add(tax_obj)
    session.commit()
    session.refresh(tax_obj)

    # return the tax object
    return tax_obj

    
@app.get("/calculate", response_model=schemas.taxall)
def read_todo_id(Name:str, Description : str, Price: int, GST: int, session: Session = Depends(get_session)):
    # Fetch todo record using id from the table    
    '''
    tax_obj = session.query(models.tax).get(id)
    # Check if there is record with the provided id, if not then Raise 404 Exception    
    if not tax_obj:
        raise HTTPException(status_code=404, detail=f"tax item with id {id} not found")
    return tax_obj 
'''
    thisdict = {
        "Name": "Mobile",
        "Description" : "Iphone 13 pro",
        "Price": 100000,
        "GST": 1800
    }
    return thisdict

   



