from fastapi import APIRouter

from .endpoints import user, security


router = APIRouter()
router.include_router(security.router, prefix="/security", tags=["security"])
router.include_router(user.router, prefix="/users", tags=["users"])

