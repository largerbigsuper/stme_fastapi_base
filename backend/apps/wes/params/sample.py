from typing import Optional
from fastapi import Query

class SampleQueryParams:
    def __init__(self, 
                 sample_id: Optional[Optional[str]] = Query(default=None, description='样本编号'),
                 batch_id: Optional[str] = Query(default=None, description='批次ID'),
                 batch_name: Optional[str] = Query(default=None, description='批次名称'),
                 lab_code: Optional[str] = Query(default=None, description='实验室代码'),
                 test_item: Optional[int] = Query(default=None, description='检测项目'),
                 sample_type: Optional[str] = Query(default=None, description='样本类型'),
                 acession_type: Optional[str] = Query(default=None, description='acession类型'),
                 sequencing_output: Optional[str] = Query(default=None, description='测序产出'),
                 alignable_percentage: Optional[str] = Query(default=None, description='可比对百分比'),
                 sequencing_depth_avg: Optional[str] = Query(default=None, description='平均测序深度'),
                 q30: Optional[str] = Query(default=None, description='Q30百分比'),
                 qc_batch: Optional[str] = Query(default=None, description='批次QC'),
                 qc_sample: Optional[str] = Query(default=None, description='样本QC'),
                 completion_time: Optional[str] = Query(default=None, description='完成时间(签发报告时间)'),
                 reviewer_id: Optional[int] = Query(default=None, description='审阅人'),
                 reviewer_time: Optional[str] = Query(default=None, description='审阅时间'),
                 review_status: Optional[str] = Query(default=None, description='审阅状态'),
                 review_result: Optional[str] = Query(default=None, description='审阅结果')
                 ):

        self.sample_id = sample_id
        self.batch_id = batch_id
        self.batch_name = batch_name
        self.lab_code = lab_code
        self.test_item = test_item
        self.sample_type = sample_type
        self.acession_type = acession_type
        self.sequencing_output = sequencing_output
        self.alignable_percentage = alignable_percentage
        self.sequencing_depth_avg = sequencing_depth_avg
        self.q30 = q30
        self.qc_batch = qc_batch
        self.qc_sample = qc_sample
        self.completion_time = completion_time
        self.reviewer_id = reviewer_id
        self.reviewer_time = reviewer_time
        self.review_status = review_status
        self.review_result = review_result
