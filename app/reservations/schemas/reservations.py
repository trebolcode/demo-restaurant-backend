from pydantic import BaseModel


class Book_Table_In(BaseModel):
    table: int
    chairs: int
    owner: str
    date: str
    hour: str
