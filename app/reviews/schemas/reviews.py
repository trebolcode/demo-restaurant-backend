from pydantic import BaseModel


class ReviewOut(BaseModel):
    id: int
    id_user: int
    rating: int
    comments: str

    class Config:
        orm_mode = True


class ReviewIn(BaseModel):
    id: int
    id_user: int
    rating: int
    comments: str

    class Config:
        orm_mode = True
