from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/health", summary="Health Check", operation_id="v1_health_check")
def health_check():
    """
    Health check endpoint for API v1.

    Path:
        GET /api/v1/health

    Returns:
        JSON object: {"status": "ok"}
    """
    return JSONResponse({"status": "ok"})
