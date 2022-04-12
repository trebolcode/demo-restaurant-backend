from fastapi import APIRouter
from pydantic import BaseModel

reservations = APIRouter()


def get_data():
    table = [
        {
            "table": 12,
            "chairs": 4,
            "owner": "Trebol Code",
            "date": "fecha",
            "hour": "hora"
        },
        {
            "table": 10,
            "chairs": 6,
            "owner": "Otra",
            "date": "fecha",
            "hour": "hora"
        },
    ]
    return table


def save_data(table):
    pass


class Book_Table_In(BaseModel):
    table: int
    chairs: int
    owner: str
    date: str
    hour: str


@reservations.get(
    path="/tables"
)
def get_all_tables():
    return get_data()


@reservations.post(
    path="/tables"
)
def book_table(table: Book_Table_In):
    save_data(table)
    return table
