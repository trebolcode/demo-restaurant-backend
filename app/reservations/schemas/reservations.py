from xmlrpc.client import boolean
from pydantic import BaseModel


class BookTableInput(BaseModel):
    id_user :int
    id_table :int
    starts_at : str
    ends_at : str
    is_available : bool
    event :str

    class Config:
        orm_mode = True

class BookTable(BookTableInput):
    id:int