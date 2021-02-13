from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

import sys
import os

from loguru import logger

from .routes import (
    healthcheck,
    notes,
    users,
    token
)
from app.db import database

if not os.getenv("SECRET_KEY"):
    logger.error("Please set the SECRET_KEY variable prior to startup.")
    sys.exit(0)

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

# v1 APIs
app.include_router(notes.router, prefix="/v1")
app.include_router(users.router, prefix="/v1")
app.include_router(token.router, prefix="/v1")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
