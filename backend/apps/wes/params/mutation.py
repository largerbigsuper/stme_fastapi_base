from typing import Optional
from fastapi import Query

class MutationQueryParams:
    def __init__(self, 
                 batch_id: Optional[str] = Query(default=None, description='批次ID'),
                 sample_id: Optional[Optional[str]] = Query(default=None, description='样本编号'),
                 gene_name: Optional[str] = Query(default=None, description='基因名称'),
                 review_status: Optional[str] = Query(default=None, description='审阅状态'),
                 review_result: Optional[str] = Query(default=None, description='审阅结果')
                 ):

        self.sample_id = sample_id
        self.batch_id = batch_id
        self.gene_name = gene_name
        self.review_status = review_status
        self.review_result = review_result
