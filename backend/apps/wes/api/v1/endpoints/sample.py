from typing import Mapping

from apps.auth import models as auth_models
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user)
from apps.wes import models, schemas, services
from apps.wes.api.deps import valid_sample_id
from apps.wes import params
from core.db.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from utils.paginations import PageResponse

router = APIRouter()

@router.post("/", response_model=schemas.Sample)
async def create(
    payload: schemas.SampleCreate,
    db: Session = Depends(get_db), 
    current_user: auth_models.User = Depends(get_current_active_superuser)):
    return await services.sample.create_sample(db, payload)

@router.get("/", response_model=PageResponse[schemas.Sample])
async def page(
    params=Depends(params.sample.SampleQueryParams),
    page: int = 1, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.sample.page(db, page=page, limit=limit, params=params)

@router.get("/{sample_id}", response_model=schemas.Sample)
async def get_sample(
    sample: Mapping = Depends(valid_sample_id), 
    current_user: auth_models.User = Depends(get_current_active_user)
    ):
    return sample

@router.delete("/{sample_id}")
async def delete_sample(
    sample_id: int, 
    db: Session = Depends(get_db), 
    sample: Mapping = Depends(valid_sample_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.sample.delete_by_id(db, sample_id)

@router.put("/{sample_id}", response_model=schemas.Sample)
async def update_sample(
    sample_id: int, 
    updates: schemas.SampleUpdate, 
    db: Session = Depends(get_db), 
    sample: Mapping = Depends(valid_sample_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.sample.update_sample(db, sample, updates)

@router.post("/{sample_id}/review_status", response_model=schemas.Sample)
async def update_sample_review_status(
    sample_id: int, 
    updates: schemas.SampleUpdate, 
    db: Session = Depends(get_db), 
    sample: Mapping = Depends(valid_sample_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.sample.update_sample_review_status(db, sample, updates)
