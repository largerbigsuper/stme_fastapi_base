from typing import Mapping

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from apps.auth import models, schemas, services
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user, valid_role_id)
from core.db.session import get_db
from utils.paginations import PageResponse

router = APIRouter()

@router.post("/", response_model=schemas.Role)
async def create_role(
    role: schemas.RoleCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.role.create_role(db=db, role=role)

@router.get("/", response_model=PageResponse[schemas.Role])
async def get_roles(
    page: int = 1, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.role.page(db, page=page, limit=limit)

@router.get("/{role_id}", response_model=schemas.Role)
async def get_role(
    role: Mapping = Depends(valid_role_id), 
    current_user: models.User = Depends(get_current_active_user)
    ):
    return role

@router.delete("/{role_id}")
async def delete_role(
    role_id: int, 
    db: Session = Depends(get_db), 
    role: Mapping = Depends(valid_role_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.role.delete_role_by_id(db, role_id=role_id)

@router.put("/{role_id}", response_model=schemas.Role)
async def update_role(
    role_id: int, 
    user: schemas.RoleUpdate, 
    db: Session = Depends(get_db), 
    role: Mapping = Depends(valid_role_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.role.update_role(db, db_obj=role, updates=user)
