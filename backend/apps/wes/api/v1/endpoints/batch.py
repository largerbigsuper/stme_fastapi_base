from typing import Mapping

from apps.auth import models as auth_models
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user)
from apps.wes import models, schemas, services
from apps.wes.api.deps import valid_batch_id
from apps.wes import params
from core.db.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils.paginations import PageResponse

router = APIRouter()

@router.post("/", response_model=schemas.Batch)
async def create_batch(
    payload: schemas.BatchCreate,
    db: Session = Depends(get_db), 
    current_user: auth_models.User = Depends(get_current_active_superuser)):
    return await services.batch.create_batch(db, payload)

@router.get("/", response_model=PageResponse[schemas.Batch])
async def page(
    params=Depends(params.batch.BatchQueryParams),
    page: int = 1, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.batch.page(db, page=page, limit=limit, params=params)

@router.get("/{batch_id}", response_model=schemas.Batch)
async def get_batch(
    batch: Mapping = Depends(valid_batch_id), 
    current_user: auth_models.User = Depends(get_current_active_user)
    ):
    return batch

@router.delete("/{batch_id}")
async def delete_batch(
    batch_id: int, 
    db: Session = Depends(get_db), 
    batch: Mapping = Depends(valid_batch_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.batch.delete_by_id(db, batch_id)

@router.put("/{batch_id}", response_model=schemas.Batch)
async def update_batch(
    batch_id: int, 
    updates: schemas.BatchUpdate, 
    db: Session = Depends(get_db), 
    batch: Mapping = Depends(valid_batch_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.batch.update_batch(db, batch, updates)

@router.post("/{batch_id}/review_status", response_model=schemas.Batch)
async def update_batch_review_status(
    batch_id: int, 
    updates: schemas.BatchUpdateReview, 
    db: Session = Depends(get_db), 
    batch: Mapping = Depends(valid_batch_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.batch.update_batch_review_status(db, batch, updates)
