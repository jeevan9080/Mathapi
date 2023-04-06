from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class tax(Base):
    __tablename__ = 'tax'
    Name: Column(String(256)) 
    Description : Column(String(256))
    Price: Column(Integer())
    GST: Column(Integer())

    