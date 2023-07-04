from typing import Any, Dict, Optional, Union
from pydantic import BaseModel

from sqlalchemy.orm import Session
from apps.auth.models.user import User
from apps.auth.schemas.user import UserCreate
from core.security import get_password_hash, verify_password

from base.curd_base import CRUDBase


class CRUDUser(CRUDBase[User]):

    def get_by_username(self, db: Session, username: str):
        return db.query(self.model).filter(self.model.username == username).first()
    
    def create(self, db: Session, obj_in: UserCreate) -> User:
        obj_in.password = get_password_hash(obj_in.password)
        return super().create(db, obj_in)

    def update(self, db: Session, db_obj: User, obj_in: BaseModel) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            update_data["password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def authenticate(self, db: Session, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
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