from typing import List

from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


class Notes(BaseModel):
    notes: List[Note]
