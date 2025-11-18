from typing import List, Optional

from src.domain.schemas.customers import Customer, CustomerCreate, CustomerUpdate


class CustomerService:
    """
    Service layer for customer operations. Wraps a repository to allow business logic
    and later replacement with DB-backed implementations.
    """

    def __init__(self, repository) -> None:
        self.repository = repository

    # PUBLIC_INTERFACE
    def list_customers(self) -> List[Customer]:
        """Return all customers."""
        return self.repository.list()

    # PUBLIC_INTERFACE
    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Return a customer by ID, or None if not found."""
        return self.repository.get(customer_id)

    # PUBLIC_INTERFACE
    def create_customer(self, payload: CustomerCreate) -> Customer:
        """Create and return a new customer."""
        return self.repository.create(payload)

    # PUBLIC_INTERFACE
    def update_customer(self, customer_id: int, payload: CustomerUpdate) -> Optional[Customer]:
        """Update and return a customer, or None if not found."""
        return self.repository.update(customer_id, payload)

    # PUBLIC_INTERFACE
    def delete_customer(self, customer_id: int) -> bool:
        """Delete a customer by ID, returning True if deleted, False if not found."""
        return self.repository.delete(customer_id)
