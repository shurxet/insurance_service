from fastapi import APIRouter
from .endpoints.insurance import router as insurance_router
from .endpoints.rate import router as rate_router
from .endpoints.cargo import router as cargo_router


api_router = APIRouter()
api_router.include_router(insurance_router, prefix="/insurance", tags=["insurance"])
api_router.include_router(rate_router, prefix="/rate", tags=["rate"])
api_router.include_router(cargo_router, prefix="/cargo", tags=["cargo"])
