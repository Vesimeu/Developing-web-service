import os

NOTES_DIR = "notes"

def get_note_path(note_id: int) -> str:
    return os.path.join(NOTES_DIR, f"{note_id}.json")
