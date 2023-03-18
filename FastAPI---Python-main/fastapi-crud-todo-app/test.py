from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    id : int
    email: str
    password: str
    phone: str
    city: str
    state: str
    country: str
    status: str


app=FastAPI()

@app.get("/")
def root():
    return{"Hello World test:3"}


