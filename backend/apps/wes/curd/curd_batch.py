
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from apps.wes.models import Batch
from apps.wes import params
from utils.paginations import paginate

from base.curd_base import CRUDBase


class CRUDBatch(CRUDBase[Batch]):

    async def get_by_name(self, db: AsyncSession, name: str):
        query = select(self.model).where(self.model.name == name).options()
        result = await db.execute(query)
        return result.scalars().one_or_none()
    
    async def page(self, db: AsyncSession, params: params.BatchQueryParams, page: int = 1, limit: int = 20):
        query = select(self.model).where()
        page = await paginate(db, query, self.model, page, limit)
        return page
        
    

batch = CRUDBatch(Batch)
