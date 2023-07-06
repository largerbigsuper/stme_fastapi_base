
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.auth import schemas, services
from apps.auth.api.deps import get_current_active_user
from apps.auth.schemas import Token, User
from core.db.session import get_db

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
    ):

    return await services.security.login(db, form_data)

@router.post("/password_change/", response_model=User)
async def password_change(payload: schemas.UserPasswordChange, 
                    current_user: Annotated[User, Depends(get_current_active_user)], 
                    db: Session = Depends(get_db)):
    
    return await services.security.password_change(db, current_user, payload)


@router.post("/password_reset/", response_model=User)
async def password_reset(payload: schemas.UserPasswordReset, db: Session = Depends(get_db)):

    return await services.security.password_reset(db, payload)


@router.get("/me/", response_model=User)
async def get_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

