from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(256))
    password = Column(String(256))
    phone = Column(String(256))
    city = Column(String(256))
    state = Column(String(256))
    country = Column(String(256))
    status = Column(String(256))

    