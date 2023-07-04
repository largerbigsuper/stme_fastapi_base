from typing import Mapping

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from apps.auth import schemas, services, models
from apps.auth.api.deps import get_current_active_superuser, get_current_active_user, valid_user_id
from core.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_active_superuser)):
    return services.user.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
def get_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.user.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schemas.User)
def get_user(
    user: Mapping = Depends(valid_user_id), 
    current_user: models.User = Depends(get_current_active_user)
    ):
    return user

@router.delete("/{user_id}")
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    user: Mapping = Depends(valid_user_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.user.delete_user_by_id(db, user_id=user_id)

@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int, 
    user: schemas.UserUpdate, 
    db: Session = Depends(get_db), 
    db_user: Mapping = Depends(valid_user_id),
    current_user: models.User = Depends(get_current_active_superuser)
    ):
    return services.user.update_user(db, db_user=db_user, updates=user)
