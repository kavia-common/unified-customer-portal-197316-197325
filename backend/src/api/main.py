from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.core.settings import get_settings
from src.api.v1.router import api_router

# Initialize settings
settings = get_settings()

app = FastAPI(
    title="Unified Customer Portal API",
    description="Versioned API for the Unified Customer Portal. Provides customers and activities endpoints.",
    version="1.0.0",
    openapi_tags=[
        {"name": "health", "description": "Health and diagnostics endpoints"},
        {"name": "customers", "description": "Customer management endpoints"},
        {"name": "activities", "description": "Customer activities endpoints"},
    ],
)

# CORS configuration based on environment settings
origins = []
if settings.FRONTEND_ORIGIN:
    origins = [settings.FRONTEND_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],  # default to * if not provided
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount versioned API router
app.include_router(api_router, prefix=settings.API_PREFIX)


# PUBLIC_INTERFACE
@app.get(f"{settings.API_PREFIX}/health", tags=["health"], summary="Health Check", operation_id="health_check")
def health_check():
    """
    Health check endpoint.

    Returns:
        JSON object indicating service status and version.
    """
    return JSONResponse({"status": "ok", "version": app.version})
