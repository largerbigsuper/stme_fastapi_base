import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from core.db.session import Base

from sqlalchemy.orm import relationship
from . import m2m

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, index=True, comment="名称")
    avatar = Column(String(150), nullable=True, comment="头像")
    sort = Column(Integer, default=99, comment="排序")
    created_by = Column(Integer, comment="创建人")
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment="创建时间")
    updated_by = Column(Integer, comment="更新人")
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment="更新时间")
    is_active = Column(Boolean, default=True)

    users = relationship("User", back_populates='roles', secondary=m2m.relationship_user_role)