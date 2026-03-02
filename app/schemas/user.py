from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from app.models.user import Role

# ====================== Запросы ======================
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# ====================== Ответы ======================
class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: Role
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True   # для SQLAlchemy 2.0

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None