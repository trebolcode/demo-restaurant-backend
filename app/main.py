from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from app.reservations.routes import reservations
from app.users.routes import users

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(reservations.router)
# app.include_router(users.router)
