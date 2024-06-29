from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Date, Index, UniqueConstraint
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False, unique=True)
    product_description = Column(String(255))
    category = Column(String(100))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    inventory_items = relationship('Inventory', back_populates='product')

    __table_args__ = (
        Index('ix_product_name', 'product_name'),
    )


class Sector(Base):
    __tablename__ = 'sectors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    location_description = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    boxes = relationship('Box', back_populates='sector')

    __table_args__ = (
        Index('ix_sector_name', 'name'),
    )


class Box(Base):
    __tablename__ = 'boxes'

    id = Column(Integer, primary_key=True)
    label = Column(String(100), nullable=False, unique=True)
    sector_id = Column(Integer, ForeignKey('sectors.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    sector = relationship('Sector', back_populates='boxes')
    inventory_items = relationship('Inventory', back_populates='box')

    __table_args__ = (
        Index('ix_label', 'label'),
    )


class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    box_id = Column(Integer, ForeignKey('boxes.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship('Product', back_populates='inventory_items')
    box = relationship('Box', back_populates='inventory_items')

    __table_args__ = (
        UniqueConstraint('product_id', 'box_id', name='uix_product_box'),
        Index('ix_product_id', 'product_id'),
        Index('ix_box_id', 'box_id'),
    )