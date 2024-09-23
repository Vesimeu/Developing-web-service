from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    text: str

class Note(BaseModel):
    id: int
    text: str
    created_at: str  # Преобразуем datetime в строку для сериализации
    updated_at: str  # Преобразуем datetime в строку для сериализации

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime
