from fastapi import APIRouter

from app.db import database, notes

from app.models.notes import (
    Notes,
    Note,
    NoteIn
)


router = APIRouter()


@router.get("/", response_model=Notes)
async def read_notes():
    query = notes.select()
    retrieved_notes = await database.fetch_all(query)
    return {"notes": retrieved_notes}


@router.post("/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
