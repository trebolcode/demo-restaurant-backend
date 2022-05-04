from pydantic import BaseModel


class Users(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    phone: str
    password: str

    class Config:
        orm_mode = True


class UsersOut(BaseModel):
    id: int
    name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class UsersIn(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str
    password: str

    class Config:
        orm_mode = True
