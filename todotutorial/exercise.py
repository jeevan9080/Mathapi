from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class Users(BaseModel):
    id : int
    email: str                    
    password: str
    phone: str
    city: str
    state: str
    country: str
    status: str


app = FastAPI()

store_users=[]

@app.get('/')
async def home():
    return{"Welcome this is the home page"}

@app.post('/users/')
async def create_users(users:Users):
    store_users.append(users)
    return users

@app.get('/users/',response_model=List[Users])
async def get_all_users():
    return store_users




