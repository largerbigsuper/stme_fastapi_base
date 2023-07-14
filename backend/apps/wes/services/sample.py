from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.wes import curd, models, schemas, params


async def get_by_id(db: AsyncSession, id: int):
    return await curd.sample.get(db, id)

async def get_by_name(db: AsyncSession, name: str):
    return await curd.sample.get_by_name(db, name)

async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await curd.sample.get_multi(db, skip, limit)

async def page(db: AsyncSession, params:params.BatchQueryParams, page: int = 1, limit: int = 100):
    return await curd.sample.page(db, page, limit, params)

async def create_sample(db: AsyncSession, payload: schemas.BatchCreate):
    db_entity = await get_by_name(db, payload.name)
    if db_entity:
        raise HTTPException(status_code=400, detail="name already exists")
    return await curd.sample.create(db, payload)

async def update_sample(db: AsyncSession, db_entity: models.Batch, updates: schemas.BatchUpdate):
    return await curd.sample.update(db, db_entity, updates)

async def update_sample_review_status(db: AsyncSession, db_entity: models.Batch, updates: schemas.SampleUpdate):
    """TODO更新review_status状态 关联更新样本，突变相关数据
    """
    return await curd.sample.update(db, db_entity, updates)

async def delete_by_id(db: AsyncSession, id: int):
    return await curd.sample.remove(db, id)

