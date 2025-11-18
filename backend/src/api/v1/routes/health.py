from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/health", summary="Health Check", operation_id="v1_health_check")
def health_check():
    """
    Health check endpoint for API v1.

    Returns:
        JSON object with ok status.
    """
    return JSONResponse({"status": "ok"})
