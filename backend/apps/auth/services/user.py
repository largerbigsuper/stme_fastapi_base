from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth import curd, models, schemas


async def get_user_by_id(db: AsyncSession, user_id: int):
    return await curd.user.get(db, user_id)

async def get_user_by_username(db: AsyncSession, username: str):
    return await curd.user.get_by_username(db, username)

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await curd.user.get_multi(db, skip, limit)

async def page(db: AsyncSession, page: int = 1, limit: int = 100):
    return await curd.user.page(db, page, limit)

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = await get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return await curd.user.create(db, user)

async def update_user(db: AsyncSession, db_user: models.User, updates: schemas.UserUpdate):
    return await curd.user.update(db, db_user, updates)

async def delete_user_by_id(db: AsyncSession, user_id: int):
    return await curd.user.remove(db, user_id)

