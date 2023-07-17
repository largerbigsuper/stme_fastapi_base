from typing import Mapping

from apps.auth import models as auth_models
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user)
from apps.wes import models, schemas, services
from apps.wes.api.deps import valid_mutation_id
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
    return await services.mutation.create_mutation(db, payload)

@router.get("/", response_model=PageResponse[schemas.Sample])
async def page(
    params=Depends(params.mutation.MutationQueryParams),
    page: int = 1, 
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.mutation.page(db, page=page, limit=limit, params=params)

@router.get("/{mutation_id}", response_model=schemas.Sample)
async def get_mutation(
    mutation: Mapping = Depends(valid_mutation_id), 
    current_user: auth_models.User = Depends(get_current_active_user)
    ):
    return mutation

@router.delete("/{mutation_id}")
async def delete_mutation(
    mutation_id: int, 
    db: Session = Depends(get_db), 
    mutation: Mapping = Depends(valid_mutation_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.mutation.delete_by_id(db, mutation_id)

@router.put("/{mutation_id}", response_model=schemas.Sample)
async def update_mutation(
    mutation_id: int, 
    updates: schemas.SampleUpdate, 
    db: Session = Depends(get_db), 
    mutation: Mapping = Depends(valid_mutation_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.mutation.update_mutation(db, mutation, updates)

@router.post("/{mutation_id}/review_status", response_model=schemas.Sample)
async def update_mutation_review_status(
    mutation_id: int, 
    updates: schemas.SampleUpdate, 
    db: Session = Depends(get_db), 
    mutation: Mapping = Depends(valid_mutation_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.mutation.update_mutation_review_status(db, mutation, updates)
