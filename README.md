# Restaurant API 🍕

This is a collaborative learning project.

| Tech       | Information                                       |
| ---------- | ------------------------------------------------- |
| Python     | [Documentation](https://www.python.org/doc/)      |
| Uvicorn    | [Documentation](https://www.uvicorn.org/)         |
| FastAPI    | [Documentation](https://fastapi.tiangolo.com/)    |
| Postgres   | [Documentation](https://www.postgresql.org/docs/) |
| SQLAlchemy | [Documentation](https://www.sqlalchemy.org/)      |

## Configuration of .env

This file is required for configuration.

| Variable           | Values        |
| ------------------ | ------------- |
| DATABASE_HOSTNAME= | postgres      |
| DATABASE_PORT=     | 5432          |
| DATABASE_PASSWORD= | trebolcode123 |
| DATABASE_NAME=     | trebolcode_db |
| DATABASE_USERNAME= | postgres      |
| POSTGRES_PASSWORD= | trebolcode123 |
| POSTGRES_DB=       | trebolcode_db |

- NOTE: Never use these values for production!

## Virtual Enviroment

It is necessary to have a virtual environment to work in

`python3 -m venv venv`

Install everything using

`python3 -m pip install --no-cache-dir -r requirements.txt`

## Developer:

You can now use docker to run the API.

First you need to build the container

`docker-compose -f Developer.yml build`

Second, run the container

`docker-compose -f Developer.yml up`

And if you want to exit you can use control+C.

## Database:

This API works with Postgres.

For only one time you need create tables in database:

`docker exec -it dev_api_restaurant bash`

Execute file create_tables.py:

`python3 create_tables.py`

## Pending:

- Design: CRUD
- Models: Input/Output
- Database: Postgres/SQLAlchemy/MongoDB/pymongo
- Auth: JWT Authentication

## API's

- Reservation
- Inventory
- Delivery
- Suscribe
- Menu
- Order
- Users

## Version 0.2.1
