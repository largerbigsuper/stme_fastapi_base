from typing import Mapping

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.wes import services
from core.db.session import get_db


async def valid_batch_id(batch_id: int, db: AsyncSession = Depends(get_db)) -> Mapping:
    batch =  await services.batch.get_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return batch
