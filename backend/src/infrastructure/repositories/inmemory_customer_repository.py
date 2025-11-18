from typing import Dict, List, Optional
from itertools import count

from src.domain.schemas.customers import Customer, CustomerCreate, CustomerUpdate


class InMemoryCustomerRepository:
    """
    In-memory repository for customers with simple CRUD operations.
    NOTE: This is a swap-in layer and can be replaced with a DB-backed repository later.
    """

    def __init__(self) -> None:
        # Seed data
        self._data: Dict[int, Customer] = {}
        self._id_seq = count(1)

        # Initial seed
        self.create(CustomerCreate(name="Alice Johnson", email="alice@example.com", phone="555-111-2222", company="Acme Inc."))
        self.create(CustomerCreate(name="Bob Smith", email="bob@example.com", phone="555-333-4444", company="Globex"))
        self.create(CustomerCreate(name="Carol Lee", email="carol@example.com", phone="555-555-6666", company="Initech",))

    def list(self) -> List[Customer]:
        return list(self._data.values())

    def get(self, customer_id: int) -> Optional[Customer]:
        return self._data.get(customer_id)

    def create(self, payload: CustomerCreate) -> Customer:
        new_id = next(self._id_seq)
        customer = Customer(id=new_id, **payload.model_dump())
        self._data[new_id] = customer
        return customer

    def update(self, customer_id: int, payload: CustomerUpdate) -> Optional[Customer]:
        existing = self._data.get(customer_id)
        if not existing:
            return None
        update_data = payload.model_dump(exclude_unset=True)
        updated = existing.model_copy(update=update_data)
        self._data[customer_id] = updated
        return updated

    def delete(self, customer_id: int) -> bool:
        if customer_id in self._data:
            del self._data[customer_id]
            return True
        return False
