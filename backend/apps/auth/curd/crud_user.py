from typing import Any, Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from typing_extensions import override

from apps.auth import curd
from apps.auth.models.user import User
from apps.auth.schemas.user import UserCreate
from base.curd_base import CRUDBase
from core.security import get_password_hash, verify_password
from utils.paginations import paginate


class CRUDUser(CRUDBase[User]):

    async def get(self, db: AsyncSession, id: Any):
        query = select(self.model).where(self.model.id == id).options(
            selectinload(self.model.roles)
        )
        result = await db.execute(query)
        return result.scalars().one_or_none()
    
    async def page(self, db: AsyncSession, page: int = 1, limit: int = 20):

        query = select(self.model).options(selectinload(self.model.roles))
        page = await paginate(db, query, self.model, page, limit)
        return page
        

    async def get_by_username(self, db: AsyncSession, username: str):
        query = select(self.model).filter(self.model.username == username)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, db: AsyncSession, obj_in: UserCreate) -> User:
        obj_in.password = get_password_hash(obj_in.password)
        db_obj = self.model(**obj_in.dict(exclude={"roles"}))  # type: ignore
        if obj_in.roles:
            role_ids = [x.id for x in obj_in.roles]
            roles = await curd.role.get_by_ids(db, role_ids)
            db_obj.roles = roles
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, db_obj: User, obj_in: BaseModel) -> User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude={"roles"})
        if "new_password" in update_data:
            hashed_password = get_password_hash(update_data["new_password"])
            del update_data["new_password"]
            update_data["password"] = hashed_password
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        # process roles
        if obj_in.roles:
            role_ids = [x.id for x in obj_in.roles]
            roles = await curd.role.get_by_ids(db, role_ids)
            db_obj.roles = roles
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        user = await self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user


    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser

user = CRUDUser(User)
