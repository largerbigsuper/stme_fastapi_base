
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    password: str
    username: str
    is_superuser: Optional[bool]
    is_active: Optional[bool]


class UserUpdate(BaseModel):
    nickname: Optional[str]
    gender: Optional[str]
    avatar: Optional[str]
    email: Optional[str]
    is_superuser: bool
    is_active: bool


class UserPassword(BaseModel):
    password: str


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

    class Config:
        orm_mode = True

