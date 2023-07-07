from datetime import timedelta

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth import curd, models, schemas, services
from core.config import settings
from core.security import create_access_token, verify_password


async def login(db: AsyncSession, form_data: OAuth2PasswordRequestForm):
    user = await curd.user.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def password_change(db: AsyncSession, current_user: models.User, payload: schemas.UserPasswordChange):
    if not verify_password(payload.password, current_user.password):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error old password")
    return await _change_password(db, current_user.username, payload.new_password)


async def password_reset(db: AsyncSession, payload: schemas.UserPasswordReset):
    CODE_DICT = {
        "admin": "888888" 
    }
    correct_code = CODE_DICT.get(payload.username)
    if not correct_code or payload.code != correct_code:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error code")
    return await _change_password(db, payload.username, payload.password)


async def _change_password(db: AsyncSession, username: str, password: str):
    db_user = await services.user.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    updates = schemas.UserPassword(new_password=password)
    return await services.user.update_user(db=db, db_user=db_user, updates=updates)