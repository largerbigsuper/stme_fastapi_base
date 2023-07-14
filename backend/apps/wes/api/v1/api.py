from fastapi import APIRouter

from .endpoints import batch, sample


router = APIRouter()
router.include_router(batch.router, prefix="/batch", tags=["batch"])
router.include_router(sample.router, prefix="/sample", tags=["sample"])
