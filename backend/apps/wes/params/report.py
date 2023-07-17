from typing import Optional
from fastapi import Query

class ReportQueryParams:
    def __init__(self, 
                 sample_id: Optional[Optional[str]] = Query(default=None, description='样本编号'),
                 lab_code: Optional[str] = Query(default=None, description='实验室代码'),
                 sample_type: Optional[str] = Query(default=None, description='样本类型'),
                 issue_status: Optional[int] = Query(default=None, description='签发状态'),
                 review_status: Optional[str] = Query(default=None, description='审阅状态'),
                 review_result: Optional[str] = Query(default=None, description='审阅结果')
                 ):

        self.sample_id = sample_id
        self.lab_code = lab_code
        self.sample_type = sample_type
        self.issue_status = issue_status
        self.review_status = review_status
        self.review_result = review_result
