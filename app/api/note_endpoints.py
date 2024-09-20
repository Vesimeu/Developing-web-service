from fastapi import APIRouter, HTTPException, Depends
from app.auth.auth import verify_token
from app.services.note_service import (
    create_note_service, get_note_service,
    get_note_info_service, update_note_service,
    delete_note_service, list_notes_service
)
from app.models.note import Note, NoteInfo

router = APIRouter()

@router.post("/notes", response_model=Note)
def create_note(text: str, token: str = Depends(verify_token)):
    return create_note_service(text)

@router.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, token: str = Depends(verify_token)):
    return get_note_service(note_id)

@router.get("/notes/{note_id}/info", response_model=NoteInfo)
def get_note_info(note_id: int, token: str = Depends(verify_token)):
    return get_note_info_service(note_id)

@router.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, text: str, token: str = Depends(verify_token)):
    return update_note_service(note_id, text)

@router.delete("/notes/{note_id}")
def delete_note(note_id: int, token: str = Depends(verify_token)):
    return delete_note_service(note_id)

@router.get("/notes", response_model=dict)
def list_notes(token: str = Depends(verify_token)):
    return list_notes_service()
