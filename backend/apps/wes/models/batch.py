import datetime
from sqlalchemy import Column, DateTime, Integer, String, TIMESTAMP
from core.db.session import Base

class Batch(Base):
    __tablename__ = 'wes_sequencing_batch'
    __table_args__ = {'comment': '测序批次'}

    id = Column(Integer, primary_key=True, comment='id')
    name = Column(String(length=900), comment='批次名称')
    sequencing_working_set = Column(String(length=255), comment='测序工作集')
    sequencing_instrument = Column(String(length=255), comment='测序仪器')
    sequencing_output = Column(String(length=900), comment='测序产出')
    q30 = Column(Integer, comment='Q30百分比')
    qc = Column(String(length=255), comment='QC质控')
    qc_positive = Column(String(length=32), comment='positive质控')
    qc_ntc = Column(String(length=32), comment='NTC质控')
    completion_time = Column(DateTime(timezone=True), comment='完成时间')
    reviewer_id = Column(Integer, comment='审阅人')
    reviewer_time = Column(DateTime(timezone=True), comment='审阅时间')
    review_status = Column(String(length=32), comment='审阅状态')
    review_result = Column(String(length=32), comment='审阅结果')
    created_by = Column(String(length=32), comment='创建人')
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment='创建时间')
    updated_by = Column(String(length=32), comment='更新人')
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment='更新时间')

