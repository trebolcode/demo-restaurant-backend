# structure db
from config.database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    email = Column(String(225), nullable=False)
    phone = Column(String(225), nullable=False)
    password = Column(String(225), nullable=False)
