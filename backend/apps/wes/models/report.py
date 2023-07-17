import datetime
from sqlalchemy import Column, DateTime, String, Integer

from core.db.session import Base


class Report(Base):
    __tablename__ = 'wes_sequencing_report'
    __table_args__ = {'comment': '报告'}

    id = Column(Integer, primary_key=True, comment='id')
    sample_id = Column(String(255), comment='批次编号')
    lab_code = Column(String(255), comment='实验室代码')
    test_item = Column(String(32), comment='检测项目')
    sample_type = Column(String(32), comment='样本类型')
    acession_type = Column(String(32), comment='accession类型')
    completion_time = Column(DateTime(timezone=True), nullable=True, comment='完成时间(签发报告时间)')
    reviewer_id = Column(Integer, comment='审阅人')
    review_time = Column(DateTime(timezone=True), nullable=True, comment='审阅时间')
    review_status = Column(Integer, default=0, comment='审阅状态')
    review_result = Column(String(32), comment='审阅结果')
    conclusion = Column(String(255), comment='报告结论')
    issue_status = Column(Integer, default=-1, comment='签发状态')
    file_url = Column(String(255), comment='报告地址')
    created_by = Column(Integer, comment='创建人')
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment='创建时间')
    updated_by = Column(Integer, comment='更新人')
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment='更新时间')

