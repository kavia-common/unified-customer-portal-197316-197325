from typing import Dict, List
from itertools import count
from datetime import datetime, timedelta

from src.domain.schemas.activities import Activity


class InMemoryActivityRepository:
    """
    In-memory repository for customer activities.
    """

    def __init__(self) -> None:
        self._id_seq = count(1)
        self._by_customer: Dict[int, List[Activity]] = {}

        # Seed activities for initial customers with IDs 1..3
        now = datetime.utcnow()
        self._by_customer[1] = [
            self._make(1, "email", "Sent welcome email", now - timedelta(days=2)),
            self._make(1, "call", "Introductory call", now - timedelta(days=1, hours=3)),
        ]
        self._by_customer[2] = [
            self._make(2, "meeting", "Product demo", now - timedelta(days=4)),
        ]
        self._by_customer[3] = []

    def _make(self, customer_id: int, type_: str, desc: str, ts: datetime) -> Activity:
        return Activity(
            id=next(self._id_seq),
            customer_id=customer_id,
            type=type_,
            description=desc,
            timestamp=ts,
        )

    def list_by_customer(self, customer_id: int) -> List[Activity]:
        return list(self._by_customer.get(customer_id, []))
