from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class student(Base):
    __tablename__ = 'student'
    id = Column(String(256))
    name = Column(String(256))

    