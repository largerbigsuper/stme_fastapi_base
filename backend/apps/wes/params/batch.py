from typing import Optional
from fastapi import Query

class BatchQueryParams:
    def __init__(self, batch_name: Optional[Optional[str]] = Query(default=None, description='批次名称'),
                 sequencing_working_set: Optional[str] = Query(default=None, description='测序工作集'),
                 sequencing_instrument: Optional[str] = Query(default=None, description='测序仪器'),
                 sequencing_output: Optional[str] = Query(default=None, description='测序产出'),
                 q30: Optional[int] = Query(default=None, description='Q30百分比'),
                 qc: Optional[str] = Query(default=None, description='QC质控'),
                 qc_positive: Optional[str] = Query(default=None, description='positive质控'),
                 qc_ntc: Optional[str] = Query(default=None, description='NTC质控'),
                 reviewer_id: Optional[int] = Query(default=None, description='审阅人'),
                 reviewer_time: Optional[str] = Query(default=None, description='审阅时间'),
                 review_status: Optional[str] = Query(default=None, description='审阅状态'),
                 review_result: Optional[str] = Query(default=None, description='审阅结果')
                 ):

        self.batch_name = batch_name
        self.sequencing_working_set = sequencing_working_set
        self.sequencing_instrument = sequencing_instrument
        self.sequencing_output = sequencing_output
        self.q30 = q30
        self.qc = qc
        self.qc_positive = qc_positive
        self.qc_ntc = qc_ntc
        self.reviewer_id = reviewer_id
        self.reviewer_time = reviewer_time
        self.review_status = review_status
        self.review_result = review_result

class SampleQueryParams:
    def __init__(self, batch_name: Optional[Optional[str]] = Query(default=None, description='批次名称'),
                 sequencing_working_set: Optional[str] = Query(default=None, description='测序工作集'),
                 sequencing_instrument: Optional[str] = Query(default=None, description='测序仪器'),
                 sequencing_output: Optional[str] = Query(default=None, description='测序产出'),
                 q30: Optional[int] = Query(default=None, description='Q30百分比'),
                 qc: Optional[str] = Query(default=None, description='QC质控'),
                 qc_positive: Optional[str] = Query(default=None, description='positive质控'),
                 qc_ntc: Optional[str] = Query(default=None, description='NTC质控'),
                 reviewer_id: Optional[int] = Query(default=None, description='审阅人'),
                 reviewer_time: Optional[str] = Query(default=None, description='审阅时间'),
                 review_status: Optional[str] = Query(default=None, description='审阅状态'),
                 review_result: Optional[str] = Query(default=None, description='审阅结果')
                 ):

        self.batch_name = batch_name
        self.sequencing_working_set = sequencing_working_set
        self.sequencing_instrument = sequencing_instrument
        self.sequencing_output = sequencing_output
        self.q30 = q30
        self.qc = qc
        self.qc_positive = qc_positive
        self.qc_ntc = qc_ntc
        self.reviewer_id = reviewer_id
        self.reviewer_time = reviewer_time
        self.review_status = review_status
        self.review_result = review_result
