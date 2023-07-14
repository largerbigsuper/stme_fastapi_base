
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SampleCreate(BaseModel):
    sample_id: str
    batch_id: str
    batch_name: Optional[str]
    lab_code: Optional[str]
    test_item: Optional[str]
    sample_type: Optional[str]
    acession_type: Optional[str]
    sequencing_output: Optional[str]
    alignable_percentage: Optional[str]
    sequencing_depth_avg: Optional[str]
    q30: Optional[int]
    qc_batch: Optional[str]
    qc_sample: Optional[str]
    completion_time: Optional[datetime]
    reviewer_id: Optional[int]
    reviewer_time:Optional[datetime]
    review_status: Optional[str]
    review_result: Optional[str]
    created_by: Optional[int]
    created_time: datetime
    updated_by: Optional[int]
    updated_time =datetime


class SampleUpdate(BaseModel):
    sample_id: str
    batch_id: str
    batch_name: Optional[str]
    lab_code: Optional[str]
    test_item: Optional[str]
    sample_type: Optional[str]
    acession_type: Optional[str]
    sequencing_output: Optional[str]
    alignable_percentage: Optional[str]
    sequencing_depth_avg: Optional[str]
    q30: Optional[int]
    qc_batch: Optional[str]
    qc_sample: Optional[str]
    completion_time: Optional[datetime]
    reviewer_id: Optional[int]
    reviewer_time:Optional[datetime]
    review_status: Optional[str]
    review_result: Optional[str]
    created_by: Optional[int]
    created_time: datetime
    updated_by: Optional[int]
    updated_time =datetime


class Sample(BaseModel):
    id: int
    sample_id: str
    batch_id: str
    batch_name: str
    lab_code: str
    test_item: str
    sample_type: str
    acession_type: str
    sequencing_output: str
    alignable_percentage: str
    int: str
    int: str
    int: str
    q30: int
    qc_batch: str
    qc_sample: str
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

