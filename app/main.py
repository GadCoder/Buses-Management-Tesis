from fastapi import FastAPI
from sqlmodel import SQLModel

from app.routes.base import api_router
from app.database.session import engine


def create_tables():
    SQLModel.metadata.create_all(bind=engine)


def include_router(app_):
    app_.include_router(api_router)


def start_application():
    app_ = FastAPI()
    create_tables()
    include_router(app_)

    return app_


app = start_application()
