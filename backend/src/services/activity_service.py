from typing import List

from src.domain.schemas.activities import Activity


class ActivityService:
    """
    Service layer for activity operations.
    """

    def __init__(self, repository) -> None:
        self.repository = repository

    # PUBLIC_INTERFACE
    def list_by_customer(self, customer_id: int) -> List[Activity]:
        """List activities for a given customer."""
        return self.repository.list_by_customer(customer_id)
