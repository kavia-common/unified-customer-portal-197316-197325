from typing import List
from fastapi import APIRouter, HTTPException, Path, status

from src.domain.schemas.customers import (
    Customer,
    CustomerCreate,
    CustomerUpdate,
)
from src.services.customer_service import CustomerService
from src.infrastructure.repositories.inmemory_customer_repository import InMemoryCustomerRepository

router = APIRouter()

# Wire service with in-memory repository (can be swapped later via DI if needed)
_service = CustomerService(repository=InMemoryCustomerRepository())


# PUBLIC_INTERFACE
@router.get(
    "",
    response_model=List[Customer],
    summary="List customers",
    description="Retrieve a list of all customers.",
    operation_id="list_customers",
)
def list_customers() -> List[Customer]:
    """
    List all customers.

    Returns:
        List[Customer]: All customers currently stored.
    """
    return _service.list_customers()


# PUBLIC_INTERFACE
@router.get(
    "/{customer_id}",
    response_model=Customer,
    summary="Get customer by ID",
    description="Retrieve a single customer by its unique identifier.",
    operation_id="get_customer_by_id",
)
def get_customer_by_id(
    customer_id: int = Path(..., description="Unique identifier of the customer"),
) -> Customer:
    """
    Get a single customer by ID.

    Args:
        customer_id: The ID of the customer.

    Returns:
        Customer: The customer if found.

    Raises:
        HTTPException: 404 if the customer is not found.
    """
    customer = _service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer


# PUBLIC_INTERFACE
@router.post(
    "",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    summary="Create customer",
    description="Create a new customer.",
    operation_id="create_customer",
)
def create_customer(payload: CustomerCreate) -> Customer:
    """
    Create a new customer.

    Args:
        payload: CustomerCreate payload with the new customer's data.

    Returns:
        Customer: The created customer.
    """
    return _service.create_customer(payload)


# PUBLIC_INTERFACE
@router.put(
    "/{customer_id}",
    response_model=Customer,
    summary="Update customer",
    description="Update an existing customer by ID.",
    operation_id="update_customer",
)
def update_customer(
    payload: CustomerUpdate,
    customer_id: int = Path(..., description="Unique identifier of the customer to update"),
) -> Customer:
    """
    Update a customer.

    Args:
        payload: Fields to update for the customer.
        customer_id: The ID of the customer to update.

    Returns:
        Customer: The updated customer.

    Raises:
        HTTPException: 404 if the customer is not found.
    """
    updated = _service.update_customer(customer_id, payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return updated


# PUBLIC_INTERFACE
@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete customer",
    description="Delete a customer by ID.",
    operation_id="delete_customer",
)
def delete_customer(
    customer_id: int = Path(..., description="Unique identifier of the customer to delete"),
) -> None:
    """
    Delete a customer.

    Args:
        customer_id: The ID of the customer to delete.

    Raises:
        HTTPException: 404 if the customer is not found.
    """
    deleted = _service.delete_customer(customer_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return None
