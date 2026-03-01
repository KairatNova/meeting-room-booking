from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Meeting Room Booking API",
    description="API для бронирования переговорных комнат (дипломный проект)",
    version="0.1.0",
)

# Разрешаем CORS для фронтенда (потом изменим на конкретный origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # для разработки — потом сузим
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API работает"}