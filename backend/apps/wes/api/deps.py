from typing import Mapping

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.wes import services
from core.db.session import get_db


async def valid_batch_id(batch_id: int, db: AsyncSession = Depends(get_db)) -> Mapping:
    obj =  await services.batch.get_by_id(db, batch_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return obj


async def valid_sample_id(sample_id: int, db: AsyncSession = Depends(get_db)) -> Mapping:
    obj =  await services.sample.get_by_id(db, sample_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return obj


async def valid_mutation_id(mutation_id: int, db: AsyncSession = Depends(get_db)) -> Mapping:
    obj =  await services.mutation.get_by_id(db, mutation_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return obj
