from fastapi import APIRouter

from src.api.v1.routes.health import router as health_router
from src.api.v1.routes.customers import router as customers_router
from src.api.v1.routes.activities import router as activities_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(customers_router, prefix="/customers", tags=["customers"])
api_router.include_router(activities_router, prefix="/customers", tags=["activities"])
