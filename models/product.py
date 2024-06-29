from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Date, Index, UniqueConstraint
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False, unique=True)
    product_description = Column(String(255))
    product_brand = Column(String(100))
    product_category = Column(String(100))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    inventory_items = relationship('Inventory', back_populates='product')

    __table_args__ = (
        Index('ix_product_name', 'product_name'),
    )


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    products = relationship('Product', back_populates='category')

    __table_args__ = (
        Index('ix_category_name', 'category_name'),
    )
    

class Sector(Base):
    __tablename__ = 'sectors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    location_description = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    inventory = relationship('Inventory', back_populates='sector')

    __table_args__ = (
        Index('ix_sector_name', 'name'),
    )


class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    sector_id = Column(Integer, ForeignKey('sectors.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship('Product', back_populates='inventory_items')
    sector = relationship('Sector', back_populates='inventory')

    __table_args__ = (
        Index('ix_product_id', 'product_id'),
        Index('ix_sector_id', 'sector_id'),
        UniqueConstraint('product_id', 'sector_id', name='uq_product_sector')
    )