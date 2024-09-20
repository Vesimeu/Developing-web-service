from pydantic import BaseModel
from datetime import datetime

class Note(BaseModel):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime
