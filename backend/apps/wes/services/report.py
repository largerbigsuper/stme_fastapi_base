from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.wes import curd, models, schemas, params


async def get_by_id(db: AsyncSession, id: int):
    return await curd.report.get(db, id)

async def get_by_name(db: AsyncSession, name: str):
    return await curd.report.get_by_name(db, name)

async def get_multi(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await curd.report.get_multi(db, skip, limit)

async def page(db: AsyncSession, params:params.ReportQueryParams, page: int = 1, limit: int = 100):
    return await curd.report.page(db, page=page, limit=limit, params=params)

async def create_report(db: AsyncSession, payload: schemas.ReportCreate):
    return await curd.report.create(db, payload)

async def update_report(db: AsyncSession, db_entity: models.Report, updates: schemas.ReportUpdate):
    return await curd.report.update(db, db_entity, updates)

async def update_report_is_issued(db: AsyncSession, db_entity: models.Report, updates: schemas.ReportIssued):
    return await curd.report.update(db, db_entity, updates)

async def delete_by_id(db: AsyncSession, id: int):
    return await curd.report.remove(db, id)

async def generate_result(db: AsyncSession, report: models.Report):
    # TODO 生成报告
    await curd.report.update(db, report, )
    return True


