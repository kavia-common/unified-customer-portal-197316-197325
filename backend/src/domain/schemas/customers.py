from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class CustomerBase(BaseModel):
    """Base fields shared by Customer schemas."""
    name: str = Field(..., description="Full name of the customer")
    email: EmailStr = Field(..., description="Primary email of the customer")
    phone: Optional[str] = Field(None, description="Phone number of the customer")
    company: Optional[str] = Field(None, description="Company name, if applicable")
    status: Optional[str] = Field(
        default="active",
        description="Lifecycle status for the customer (e.g., active, inactive, prospect)",
    )


class CustomerCreate(CustomerBase):
    """Payload for creating a new customer."""
    pass


class CustomerUpdate(BaseModel):
    """Payload for updating an existing customer."""
    name: Optional[str] = Field(None, description="Full name of the customer")
    email: Optional[EmailStr] = Field(None, description="Primary email of the customer")
    phone: Optional[str] = Field(None, description="Phone number of the customer")
    company: Optional[str] = Field(None, description="Company name, if applicable")
    status: Optional[str] = Field(None, description="Lifecycle status for the customer (e.g., active, inactive, prospect)")


class Customer(CustomerBase):
    """Customer data returned by the API."""
    id: int = Field(..., description="Unique identifier of the customer")
