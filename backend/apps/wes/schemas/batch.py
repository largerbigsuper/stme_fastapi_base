
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BatchUpdateReview(BaseModel):
    review_status: str

class BatchCreate(BaseModel):
    name: str
    sequencing_working_set: Optional[str]
    sequencing_instrument: Optional[str] = 100
    sequencing_output: Optional[str]
    q30: Optional[int] = 100
    qc: Optional[str]
    qc_positive: Optional[str]
    qc_ntc: Optional[str]


class BatchUpdate(BaseModel):
    sequencing_working_set: Optional[str]
    sequencing_instrument: Optional[str] = 100
    sequencing_output: Optional[str]
    q30: Optional[int] = 100
    qc: Optional[str]
    qc_positive: Optional[str]
    qc_ntc: Optional[str]


class Batch(BaseModel):
    id: int
    name: str
    sequencing_working_set: str
    sequencing_instrument: str
    sequencing_output: str
    q30: int
    qc: str
    qc_positive: str
    qc_ntc: str
    completion_time: Optional[datetime]
    reviewer_id: Optional[int]
    reviewer_time:Optional[datetime]
    review_status: Optional[str]
    review_result: Optional[str]
    created_by: Optional[int]
    created_time: datetime
    updated_by: Optional[int]
    updated_time =datetime

    class Config:
        orm_mode = True

