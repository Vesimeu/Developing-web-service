import os
import json
from datetime import datetime
from app.utils.file_operations import get_note_path
from app.models.note import Note, NoteInfo
from fastapi import HTTPException

NOTES_DIR = "notes"

def create_note_service(text: str) -> Note:
    #А вдруг её нет
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

    note_id = len(os.listdir(NOTES_DIR)) + 1
    note_data = {
        "id": note_id,
        "text": text,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    with open(get_note_path(note_id), "w") as f:
        json.dump(note_data, f)
    return Note(**note_data)

def get_note_service(note_id: int) -> Note:
    try:
        with open(get_note_path(note_id), "r") as f:
            note_data = json.load(f)
        return Note(**note_data)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

def get_note_info_service(note_id: int) -> NoteInfo:
    note = get_note_service(note_id)
    return NoteInfo(created_at=note.created_at, updated_at=note.updated_at)

def update_note_service(note_id: int, text: str) -> Note:
    note = get_note_service(note_id)
    note.text = text
    note.updated_at = datetime.now().isoformat()
    with open(get_note_path(note_id), "w") as f:
        json.dump(note.dict(), f)
    return note

def delete_note_service(note_id: int):
    try:
        os.remove(get_note_path(note_id))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

def list_notes_service() -> dict:
    notes = os.listdir(NOTES_DIR)
    note_ids = {i: int(note.split(".")[0]) for i, note in enumerate(notes)}
    return note_ids
