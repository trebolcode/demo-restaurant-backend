from fastapi import APIRouter

# Schema
import app.reservations.schemas as schema

# Model
import app.reservations.models as model

router = APIRouter()


@router.get(
    path="/tables"
)
def get_all_tables():
    return {"msg": "info about tables"}


@router.post(
    path="/tables"
)
def book_table(table: schema.Book_Table_In):
    return table
