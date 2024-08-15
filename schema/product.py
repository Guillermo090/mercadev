from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    id : Optional[int] = Field(None)
    category_name : str = Field(..., max_length=100)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class Sector(BaseModel):
    id : Optional[int] = Field(None)
    name : str = Field(..., max_length=100)
    location_description : Optional[str] = Field(None, max_length=255)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class Product(BaseModel):
    id : Optional[int] = Field(None)
    product_name : str = Field(..., max_length=100)
    brand : Optional[str] = Field(None, max_length=100)
    product_description : Optional[str] = Field(None, max_length=255)
    category_id: Optional[int] = Field(None)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)


class Inventory(BaseModel):
    id : Optional[int] = Field(None)
    product_id: int = Field(...)
    sector_id: Optional[int] = Field(None)
    quantity : Optional[int] = Field(None)
    expiration_date : Optional[datetime] = Field(None)
    created_at: Optional[datetime] = Field(None)
    updated_at: Optional[datetime] = Field(None)