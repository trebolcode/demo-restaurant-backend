import motor.motor_asyncio
from app.reservations.models.model import Book_Table_In


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.Restaurant
collection = database.tables

async def fetch_one_table(table):
    document = await collection.find_one({"table": table})
    return document

async def fetch_all_tables():
    todos_tables = []
    cursor = collection.find({})
    async for document in cursor:
        todos_tables.append(Book_Table_In(**document))
    return todos_tables

async def create_table(newtable):
    document = newtable
    result = await collection.insert_one(document)
    return document
