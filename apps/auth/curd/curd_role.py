
from sqlalchemy.orm import Session
from apps.auth.models import Role

from base.curd_base import CRUDBase


class CRUDUser(CRUDBase[Role]):

    def get_by_name(self, db: Session, name: str):
        return db.query(self.model).filter(self.model.name == name).first()

    def is_active(self, user: Role) -> bool:
        return user.is_active


role = CRUDUser(Role)
