from pydantic import BaseModel
from pydantic import BaseModel, EmailStr, Field


class Users(BaseModel):
    phone: int = Field(..., example=573000000000)
    password: str = Field(..., example="**********")

    class Config:
        orm_mode = True


class UsersOut(Users):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Juan")
    last_name: str = Field(..., example="Perez")
    email: EmailStr = Field(..., example="example@email.com")


class UsersIn(BaseModel):
    name: str = Field(..., example="Juan")
    last_name: str = Field(..., example="Perez")
    email: EmailStr = Field(..., example="example@email.com")
    phone: int = Field(..., example=573000000000)
    password: str = Field(..., example="**********")

    class Config:
        orm_mode = True
