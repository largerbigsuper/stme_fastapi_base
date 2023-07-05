from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.auth import curd, schemas, models


def get_role_by_id(db: Session, role_id: int):
    return curd.role.get(db, role_id)

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return curd.role.get_multi(db, skip, limit)

def create_role(db: Session, role: schemas.RoleCreate):
    db_obj = curd.role.get_by_name(db, role.name)
    if db_obj:
        raise HTTPException(status_code=400, detail="{name} already registered".format(name=role.name))
    return curd.role.create(db, role)

def update_role(db: Session, db_obj: models.Role, updates: schemas.RoleUpdate):
    return curd.role.update(db, db_obj, updates)

def delete_role_by_id(db: Session, role_id: int):
    return curd.role.remove(db, role_id)

def page(db: Session, page: int = 1, limit: int = 100):
    return curd.role.page(db, page, limit)