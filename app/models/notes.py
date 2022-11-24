from pydantic import BaseModel

from typing import List


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


class Notes(BaseModel):
    notes: List[Note]
