from pydantic import BaseModel

# Complete ToDo Schema (Pydantic Model)
class taxcreate(BaseModel):
    Name:str 
    Description : str
    Price: int
    GST: int
   


class taxall(BaseModel):
    Name:str 
    Description : str
    Price: int
    GST: int

    class Config:
        orm_mode=True