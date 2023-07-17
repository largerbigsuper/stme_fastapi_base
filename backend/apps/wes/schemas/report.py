from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReportBase(BaseModel):
    id: int
    sample_id: str
    lab_code: str
    test_item: str
    sample_type: str
    acession_type: str
    completion_time: Optional[datetime]
    reviewer_id: Optional[int]
    review_time: Optional[datetime]
    review_status: int
    review_result: str
    conclusion: str
    issue_status: int
    file_url: str
    created_by: Optional[int]
    created_time: datetime
    updated_by: Optional[int]
    updated_time: datetime


class ReportCreate(BaseModel):
    sample_id: str
    lab_code: str
    test_item: str
    sample_type: str
    acession_type: str
    completion_time: Optional[datetime]
    reviewer_id: Optional[int]
    review_time: Optional[datetime]
    review_status: Optional[int]
    review_result: Optional[str]
    conclusion: Optional[str]
    issue_status: int
    file_url: Optional[str]


class ReportUpdate(ReportBase):
    pass

class ReportIssued(BaseModel):
    issue_status: int


class Report(ReportBase):
    class Config:
        orm_mode = True