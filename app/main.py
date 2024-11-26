from fastapi import FastAPI
from sqlmodel import SQLModel

from routes.base import api_router
from database.session import engine


def create_tables():
    SQLModel.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)

    return app


app = start_application()
