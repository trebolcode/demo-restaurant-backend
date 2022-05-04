# structure db
from config.database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime


class Reservations(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, nullable=False)
    id_user = Column(Integer, nullable=False)
    id_table = Column(Integer, nullable=False)
    starts_at = Column(String(255), nullable=False)
    ends_at = Column(String(255), nullable=False)
    is_available = Column(Boolean, nullable=False)
    event = Column(String(255))
