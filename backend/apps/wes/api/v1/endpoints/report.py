from typing import Mapping

from apps.auth import models as auth_models
from apps.auth.api.deps import (get_current_active_superuser,
                                get_current_active_user)
from apps.wes import models, params, schemas, services
from apps.wes.api.deps import valid_report_id
from core.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from apps.wes.models import enums

from utils.paginations import PageResponse

router = APIRouter()

@router.post("/", response_model=schemas.Report)
async def create(
    payload: schemas.ReportCreate,
    db: Session = Depends(get_db), 
    current_user: auth_models.User = Depends(get_current_active_superuser)):
    return await services.report.create_report(db, payload)

@router.get("/", response_model=PageResponse[schemas.Report])
async def page(
    params=Depends(params.ReportQueryParams),
    page: int = 1, 
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.report.page(db, page=page, limit=limit, params=params)

@router.get("/{report_id}", response_model=schemas.Report)
async def get_report(
    report: Mapping = Depends(valid_report_id), 
    current_user: auth_models.User = Depends(get_current_active_user)
    ):
    return report

@router.delete("/{report_id}")
async def delete_report(
    report_id: int, 
    db: Session = Depends(get_db), 
    report: Mapping = Depends(valid_report_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.report.delete_by_id(db, report_id)

@router.put("/{report_id}", response_model=schemas.Report)
async def update_report(
    report_id: int, 
    updates: schemas.ReportUpdate, 
    db: Session = Depends(get_db), 
    report: Mapping = Depends(valid_report_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.report.update_report(db, report, updates)

@router.post("/{report_id}/issued", response_model=schemas.Report, name="签发报告")
async def update_report_is_issued(
    report_id: int, 
    updates: schemas.ReportIssued, 
    db: Session = Depends(get_db), 
    report: Mapping = Depends(valid_report_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    return await services.report.update_report_is_issued(db, report, updates)

@router.post("/{report_id}/generate_result", name="生成报告")
async def generate_result(
    report_id: int, 
    db: Session = Depends(get_db), 
    report: models.Report = Depends(valid_report_id),
    current_user: auth_models.User = Depends(get_current_active_superuser)
    ):
    if report.issue_status == enums.IssueStatusEnum.SUCCESS:
        return HTTPException(status_code=400, detail="已签发的报告不能重新生成报告结果")
    return await services.report.generate_result(db, report)
