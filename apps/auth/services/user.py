from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.auth import curd, schemas, models


def get_user_by_id(db: Session, user_id: int):
    return curd.user.get(db, user_id)

def get_user_by_username(db: Session, username: str):
    return curd.user.get_by_username(db, username)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return curd.user.get_multi(db, skip, limit)

def create_user(db: Session, user: schemas.UserCreate):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return curd.user.create(db, user)

def update_user(db: Session, db_user: models.User, updates: schemas.UserUpdate):
    return curd.user.update(db, db_user, updates)

def delete_user_by_id(db: Session, user_id: int):
    return curd.user.remove(db, user_id)

