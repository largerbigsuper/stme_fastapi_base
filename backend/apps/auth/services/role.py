from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from apps.auth import curd, models, schemas


async def get_role_by_id(db: AsyncSession, role_id: int):
    return await curd.role.get(db, role_id)

async def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return await curd.role.get_multi(db, skip, limit)

async def create_role(db: Session, role: schemas.RoleCreate):
    db_obj = await curd.role.get_by_name(db, role.name)
    if db_obj:
        raise HTTPException(status_code=400, detail="{name} already registered".format(name=role.name))
    return await curd.role.create(db, role)

async def update_role(db: Session, db_obj: models.Role, updates: schemas.RoleUpdate):
    return await curd.role.update(db, db_obj, updates)

async def delete_role_by_id(db: Session, role_id: int):
    return await curd.role.remove(db, role_id)

async def page(db: Session, page: int = 1, limit: int = 100):
    return await curd.role.page(db, page, limit)