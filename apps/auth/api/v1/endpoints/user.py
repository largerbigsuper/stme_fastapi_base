from typing import Mapping

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from apps.auth import models, schemas, services
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user, valid_user_id)
from core.db.session import get_db
from utils.paginations import PageResponse

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_active_superuser)):
    return await services.user.create_user(db=db, user=user)

@router.get("/", response_model=PageResponse[schemas.User])
async def get_users(
    page: int = 1, 
    limit: int = 20, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.user.page(db, page=page, limit=limit)


@router.get("/{user_id}", response_model=schemas.User)
async def get_user(
    user: Mapping = Depends(valid_user_id), 
    current_user: models.User = Depends(get_current_active_user)
    ):
    return user

@router.delete("/{user_id}")
async def delete_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    user: Mapping = Depends(valid_user_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.user.delete_user_by_id(db, user_id=user_id)


@router.put("/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int, 
    user: schemas.UserUpdate, 
    db: Session = Depends(get_db), 
    db_user: Mapping = Depends(valid_user_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return await services.user.update_user(db, db_user=db_user, updates=user)
