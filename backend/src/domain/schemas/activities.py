from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Activity(BaseModel):
    """Activity associated with a customer."""
    id: int = Field(..., description="Unique identifier of the activity")
    customer_id: int = Field(..., description="Foreign key to the related customer")
    type: str = Field(..., description="Type of activity (e.g., call, email, meeting)")
    description: Optional[str] = Field(None, description="Short description of the activity")
    timestamp: datetime = Field(..., description="When the activity occurred")
