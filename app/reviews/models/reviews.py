# structure db
from config.database import Base
from sqlalchemy import ForeignKey, String, Boolean, Integer, Column, Text, DateTime
from sqlalchemy.sql.expression import text


class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(
        "Users.id", ondelete="CASCADE"), primary_key=True)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=text('now()'))
    comments = Column(String(255), nullable=False)
