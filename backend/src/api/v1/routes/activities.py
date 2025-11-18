from typing import List
from fastapi import APIRouter, Path

from src.domain.schemas.activities import Activity
from src.services.activity_service import ActivityService
from src.infrastructure.repositories.inmemory_activity_repository import InMemoryActivityRepository

router = APIRouter()

_service = ActivityService(repository=InMemoryActivityRepository())


# PUBLIC_INTERFACE
@router.get(
    "/{customer_id}/activities",
    response_model=List[Activity],
    summary="List activities for a customer",
    description="Retrieve a list of activities for the specified customer.",
    operation_id="list_customer_activities",
)
def list_customer_activities(
    customer_id: int = Path(..., description="Unique identifier of the customer"),
) -> List[Activity]:
    """
    List activities for a customer.

    Args:
        customer_id: The ID of the customer.

    Returns:
        List[Activity]: Activities for the customer.
    """
    # For in-memory seed: treat non-existing customers as empty list rather than 404,
    # unless strict behavior preferred. We'll check via repository convenience method.
    activities = _service.list_by_customer(customer_id)
    return activities
