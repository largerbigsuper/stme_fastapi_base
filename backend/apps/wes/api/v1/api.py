from fastapi import APIRouter

from .endpoints import batch, sample, mutation


router = APIRouter()
router.include_router(batch.router, prefix="/batch", tags=["batch"])
router.include_router(sample.router, prefix="/sample", tags=["sample"])
router.include_router(mutation.router, prefix="/mutation", tags=["mutation"])
