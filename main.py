from fastapi import FastAPI
from app.api import note_endpoints


app = FastAPI()

# Подключаем роутеры
app.include_router(note_endpoints.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True) # Стартуем!
