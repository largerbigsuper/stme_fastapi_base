
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str
    avatar: Optional[str]
    sort: Optional[int] = 100
    is_active: Optional[bool] = True


class RoleUpdate(BaseModel):
    name: str
    avatar: Optional[str]
    sort: Optional[int]
    is_active: Optional[bool] = True



class Role(BaseModel):
    id: int
    name: str
    sort: int
    avatar: str
    is_active: bool
    created_time: datetime
    updated_time =datetime
    last_login = datetime

    class Config:
        orm_mode = True

