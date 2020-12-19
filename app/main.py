from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

# from loguru import logger

from .routes import (
    healthcheck,
    notes,
    root
)
from app.db import database

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcheck.router, prefix="/healthcheck")
app.include_router(notes.router, prefix="/notes")
app.include_router(root.router, prefix="")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
