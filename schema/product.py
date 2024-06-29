from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id : Optional[int] = Field(None)
    product_name : str = Field(..., max_length=100)
    product_description : Optional[str] = Field(None, max_length=255)
    category: Optional[str] = Field(None, max_length=100)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)