from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import json

# from loguru import logger

from app.db import database, notes


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


class Notes(BaseModel):
    notes: List[Note]


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes", response_model=Notes)
async def read_notes():
    query = notes.select()
    retrieved_notes = await database.fetch_all(query)
    return {"notes": retrieved_notes}


@app.post("/notes", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


@app.get("/")
def root():
    return {"msg": "Hello World"}


@app.get("/healthcheck")
async def healthcheck():
    cause = []

    resp = await database.fetch_one("select 1")
    if resp[0] != 1:
        cause.append("BAD_DB")

    if len(cause) == 0:
        return {"status": "OK"}
    else:
        return HTTPException(
            status_code=500,
            detail=json.dumps(cause)
        )
