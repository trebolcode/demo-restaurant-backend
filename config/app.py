from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from app.reservations.routes import reservations
from app.users.routes import users

def get_application():

    app = FastAPI(
        title="Restaurant API",
        description="Collaborative project - Trebolcode",
        docs_url="/",
        version="0.2.0"
    )

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
    
    return app

application = get_application()
