from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "super-secret-key-change-in-production-2026"  # ОБЯЗАТЕЛЬНО поменяй в .env!

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()