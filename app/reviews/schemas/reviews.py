from pydantic import BaseModel,EmailStr, Field
from datetime import datetime

class Review(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReviewOut(Review):
    title: str = Field(...,example="The best food in history.")
    id_user: int = Field(...,example=1)
    rating: int = Field(...,example=5)
    comments: str = Field(...,example="Dont doubt come here.")
    created_at: datetime


class ReviewIn(BaseModel):
    id_user: int
    title: str
    rating: int
    comments: str

    class Config:
        orm_mode = True



class ReviewOutUser(BaseModel):
    id:int
    title: str = Field(...,example="The best food in history.")
    rating: int = Field(...,example=5)
    comments: str = Field(...,example="Dont doubt come here.")
    created_at:str
    name:str = Field(...,example="Pedro")
    last_name:str = Field(...,example="Gil")

    class Config:
        orm_mode = True