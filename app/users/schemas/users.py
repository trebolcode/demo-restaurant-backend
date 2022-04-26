from xmlrpc.client import boolean
from pydantic import BaseModel


class Users(BaseModel):
    id :int
    name :str
    last_name : str
    email : str
    phone : str
    password: str

    class Config:
        orm_mode = True

