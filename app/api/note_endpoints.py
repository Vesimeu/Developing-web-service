from fastapi import APIRouter, HTTPException, Depends, Header
from app.auth.token_auth import verify_token
from app.controller.note_service import (
    create_note_service, get_note_service,
    get_note_info_service, update_note_service,
    delete_note_service, list_notes_service
)
from app.models.note import Note, NoteInfo, NoteCreate

router = APIRouter()

"""
Это сервис в котором находятся все основные контроллеры.
"""
@router.post("/notes", response_model=Note)
def create_note(note: NoteCreate, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")  # Извлекаем токен из заголовка Authorization
    verify_token(token)  # Проверяем токен
    print("Пришёл запрос с данными токеном: " + token)
    return create_note_service(note.text)

@router.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return get_note_service(note_id)

@router.get("/notes/{note_id}/info", response_model=NoteInfo)
def get_note_info(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return get_note_info_service(note_id)

@router.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: NoteCreate, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return update_note_service(note_id, note.text)

@router.delete("/notes/{note_id}")
def delete_note(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return delete_note_service(note_id)

@router.get("/notes", response_model=dict)
def list_notes(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return list_notes_service()