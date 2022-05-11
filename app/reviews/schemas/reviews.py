from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class Review(BaseModel):
    id: int = Field(example=1)

    class Config:
        orm_mode = True


class ReviewOut(Review):
    title: str = Field(..., example="The best food in history.")
    id_user: int = Field(..., example=1)
    rating: int = Field(..., example=5)
    comments: str = Field(..., example="Dont doubt come here.")
    created_at: datetime = Field(example="2022-05-11T00:25:03.508307+00:00")


class ReviewIn(BaseModel):
    id_user: int = Field(example=1)
    title: str = Field(..., example="The best food in history.")
    rating: int = Field(..., example=5)
    comments: str = Field(..., example="Dont doubt come here.")

    class Config:
        orm_mode = True


class ReviewOutUser(BaseModel):
    id: int = Field(example=1)
    title: str = Field(..., example="The best food in history.")
    rating: int = Field(..., example=5)
    comments: str = Field(..., example="Dont doubt come here.")
    created_at: datetime = Field(example="2022-05-11T00:25:03.508307+00:00")
    name: str = Field(..., example="Pedro")
    last_name: str = Field(..., example="Gil")

    class Config:
        orm_mode = True
