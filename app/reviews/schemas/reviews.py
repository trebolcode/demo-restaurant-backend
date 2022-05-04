from pydantic import BaseModel
from datetime import datetime


class ReviewOut(BaseModel):
    id: int
    title: str
    id_user: int
    rating: int
    comments: str
    created_at: datetime

    class Config:
        orm_mode = True


class ReviewIn(BaseModel):
    id_user: int
    title: str
    rating: int
    comments: str

    class Config:
        orm_mode = True
