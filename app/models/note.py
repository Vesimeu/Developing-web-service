from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    text: str

class Note(BaseModel):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime
