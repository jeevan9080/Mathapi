from pydantic import BaseModel

# Complete ToDo Schema (Pydantic Model)
class studentcreate(BaseModel):
    name: str
   

class studentall(BaseModel):
    id : str
    name: str

    class Config:
        orm_mode=True