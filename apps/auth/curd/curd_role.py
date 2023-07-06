
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from apps.auth.models import Role

from base.curd_base import CRUDBase


class CRUDUser(CRUDBase[Role]):

    async def get_by_name(self, db: AsyncSession, name: str):
        query = select(self.model).filter(self.model.name == name)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    def is_active(self, user: Role) -> bool:
        return user.is_active


role = CRUDUser(Role)
