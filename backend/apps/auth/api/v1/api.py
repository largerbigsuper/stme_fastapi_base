from fastapi import APIRouter

from .endpoints import user, security, role, captcha


router = APIRouter()
router.include_router(security.router, prefix="/security", tags=["security"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(role.router, prefix="/roles", tags=["roles"])
router.include_router(captcha.router, prefix="/captcha", tags=["captcha"])
