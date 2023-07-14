import datetime
from sqlalchemy import DateTime, create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from core.db.session import Base


# 定义模型类
class Sample(Base):
    __tablename__ = 'wes_sequencing_sample'
    # __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, comment='id')
    sample_id = Column(String(120), comment='样本编号')
    batch_id = Column(String(120), comment='批次ID')
    batch_name = Column(String(120), comment='批次名称')
    lab_code = Column(String(120), comment='实验室代码')
    test_item = Column(String(120), comment='检测项目')
    sample_type = Column(String(120), comment='样本类型')
    acession_type = Column(String(120), comment='acession类型')
    sequencing_output = Column(String(120), comment='测序产出')
    alignable_percentage = Column(Integer, comment='可比对百分比')
    sequencing_depth_avg = Column(Integer, comment='平均测序深度')
    q30 = Column(Integer, comment='Q30百分比')
    qc_batch = Column(String(120), comment='批次QC')
    qc_sample = Column(String(120), comment='样本QC')
    completion_time = Column(DateTime(timezone=True), comment='完成时间(签发报告时间)')
    reviewer_id = Column(Integer, comment='审阅人')
    reviewer_time = Column(DateTime(timezone=True), comment='审阅时间')
    review_status = Column(String(120), comment='审阅状态')
    review_result = Column(String(120), comment='审阅结果')
    created_by = Column(String(32), comment='创建人')
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment='创建时间')
    updated_by = Column(String(32), comment='更新人')
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment='更新时间')

