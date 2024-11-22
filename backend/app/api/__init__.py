from fastapi import APIRouter
from .endpoints.insurance import router as insurance_router


api_router = APIRouter()
api_router.include_router(insurance_router, prefix="/insurance", tags=["insurance"])
