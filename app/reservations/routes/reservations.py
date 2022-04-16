from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from app.reservations.models.model import Book_Table_In


reservations = APIRouter()


from app.reservations.database.database import (
     fetch_one_table,
     fetch_all_tables,
     create_table,  
)






@reservations.get(
    path="/tables"
)
async def get_all_tables():
    response = await fetch_all_tables()
    return response




@reservations.post(
    path="/tables",
    response_model=Book_Table_In
)
async def post_reservations(newtable:Book_Table_In):
    response = await create_table(newtable.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")