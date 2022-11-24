from fastapi import APIRouter, HTTPException

from app.db import database, notes

from app.models.notes import (
    Notes,
    Note,
    NoteIn
)

from loguru import logger


router = APIRouter()


@router.get("/notes", response_model=Notes)
async def read_notes():
    query = notes.select()
    retrieved_notes = await database.fetch_all(query)

    logger.debug(f"Retrieved Notes: {retrieved_notes}")

    return {"notes": retrieved_notes}


@router.get("/notes/{note_id}", response_model=Note)
async def read_note(note_id):
    query = notes.select().where(notes.c.id == note_id)
    retrieved_note = await database.fetch_one(query)

    logger.debug(f"Retrieved Note: {retrieved_note}")

    if not retrieved_note:
        raise HTTPException(status_code=404, detail="Note not found")
    else:
        return retrieved_note


@router.post("/notes", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


@router.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    response = await database.execute(query)
    if response == 1:
        logger.debug(f"Note {note_id} deleted.")
        return {"ok": True}
    else:
        logger.debug(f"Unable to delete note {note_id}.")
        raise HTTPException(status_code=404, detail="Note not found")
