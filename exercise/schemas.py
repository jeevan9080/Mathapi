from pydantic import BaseModel

# Complete ToDo Schema (Pydantic Model)
class usercreate(BaseModel):
    email: str
    password: str
    phone: str
    city: str
    state: str
    country: str
    status: str

class userall(BaseModel):
    id : int
    email: str
    password: str
    phone: str
    city: str
    state: str
    country: str
    status: str

    class Config:
        orm_mode=True