# structure db
from config.database import Base
from sqlalchemy import ForeignKey, String, Boolean, Integer, Column, Text, DateTime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Reviews(Base):
    __tablename__ = 'Reviews'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=text('now()'))
    comments = Column(String(255), nullable=False)
    id_user = Column(Integer, ForeignKey(
        "Users.id", ondelete="CASCADE"), nullable=False)

    review_user = relationship("Users")