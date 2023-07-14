
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from apps.wes.models import Sample
from apps.wes import params
from utils.paginations import paginate

from base.curd_base import CRUDBase


class CRUDSample(CRUDBase[Sample]):

    async def get_by_name(self, db: AsyncSession, name: str):
        query = select(self.model).where(self.model.sample_id == name).options()
        result = await db.execute(query)
        return result.scalars().one_or_none()
    
    async def page(self, db: AsyncSession, params: params.SampleQueryParams, page: int = 1, limit: int = 20):
        query = select(self.model).where()
        page = await paginate(db, query, self.model, page, limit)
        return page
        
    

sample = CRUDSample(Sample)
