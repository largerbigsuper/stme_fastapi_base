from typing import Mapping

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from apps.auth import schemas, services, models
from apps.auth.api.deps import get_current_active_superuser, get_current_active_user, valid_role_id
from core.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(
    role: schemas.RoleCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_active_superuser)):
    return services.role.create_role(db=db, role=role)

@router.get("/", response_model=list[schemas.Role])
def get_roles(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.role.get_roles(db, skip=skip, limit=limit)

@router.get("/{role_id}", response_model=schemas.Role)
def get_role(
    role: Mapping = Depends(valid_role_id), 
    current_user: models.User = Depends(get_current_active_user)
    ):
    return role

@router.delete("/{role_id}")
def delete_role(
    role_id: int, 
    db: Session = Depends(get_db), 
    role: Mapping = Depends(valid_role_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.role.delete_role_by_id(db, role_id=role_id)

@router.put("/{role_id}", response_model=schemas.Role)
def update_role(
    role_id: int, 
    user: schemas.RoleUpdate, 
    db: Session = Depends(get_db), 
    role: Mapping = Depends(valid_role_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.role.update_role(db, db_obj=role, updates=user)
