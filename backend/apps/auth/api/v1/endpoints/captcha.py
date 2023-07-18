
from fastapi import APIRouter

from apps.auth import services

router = APIRouter()

@router.get("/")
async def generate_captcha():
    return await services.captcha.get_captcha()