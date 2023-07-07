
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from apps.auth.schemas import role

class UserCreate(BaseModel):
    password: str
    username: str
    is_superuser: Optional[bool]
    is_active: Optional[bool]
    roles: Optional[List[role.RoleInfo]]


class UserUpdate(BaseModel):
    nickname: Optional[str]
    gender: Optional[str]
    avatar: Optional[str]
    email: Optional[str]
    new_password: Optional[str]
    is_superuser: bool
    is_active: bool
    roles: Optional[List[role.RoleInfo]]

class UserPassword(BaseModel):
    new_password: str


class UserPasswordChange(BaseModel):
    password: str
    new_password: str


class UserPasswordReset(BaseModel):
    password: str
    username: str
    code: str


class User(BaseModel):
    id: int
    username: str
    nickname: Optional[str]
    gender: Optional[str]
    avatar: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_superuser: bool
    is_active: bool
    created_time: datetime
    updated_time =datetime
    last_login = datetime

    roles: List[role.Role]

    class Config:
        orm_mode = True

