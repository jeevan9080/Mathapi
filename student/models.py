from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class student(Base):
    __tablename__ = 'Student Model'
    id = Column(String(256), primary_key=True)
    name = Column(String(256))

    