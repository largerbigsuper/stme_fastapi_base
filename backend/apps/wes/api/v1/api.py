from fastapi import APIRouter

from .endpoints import batch


router = APIRouter()
router.include_router(batch.router, prefix="/batch", tags=["batch"])
