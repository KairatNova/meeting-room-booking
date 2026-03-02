
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError
from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User, Role
from app.schemas.user import UserRead
from sqlalchemy import select

async def get_current_user(
    token: str = Depends(lambda x: x.headers.get("Authorization")),  # Bearer token
    db: AsyncSession = Depends(get_db)
) -> User:
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Не авторизован")
    
    token = token.split(" ")[1]
    token_data = await decode_access_token(token)
    if token_data is None or token_data.email is None:
        raise HTTPException(status_code=401, detail="Неверный токен")

    result = await db.execute(select(User).where(User.email == token_data.email))
    user = result.scalar_one_or_none()

    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="Пользователь не найден или неактивен")
    
    return user


def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав (требуется admin)")
    return current_user