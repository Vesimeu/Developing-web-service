import json
from fastapi import HTTPException

TOKENS_FILE = "tokens.json"

def verify_token(token: str):
    with open(TOKENS_FILE, "r") as f:
        tokens = json.load(f)
    if token not in tokens.values():
        raise HTTPException(status_code=403, detail="Invalid token")
    return token
