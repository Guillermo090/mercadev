from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date, timedelta
import random

# Importar las clases de modelo
from models.product import Product,Category, Inventory, Sector

from sqlalchemy.ext.declarative import declarative_base
Base= declarative_base()
# Crear motor de base de datos (cambiar 'sqlite:///test.db' por tu base de datos)
engine = create_engine('sqlite:///mercadev.sqlite')

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear datos de ejemplo
categories = [
    Category(category_name='Electronics'),
    Category(category_name='Clothing'),
    Category(category_name='Home Appliances'),
]

products = [
    Product(product_name='Smartphone', brand='BrandA', product_description='Latest model', category=categories[0]),
    Product(product_name='T-Shirt', brand='BrandB', product_description='100% cotton', category=categories[1]),
    Product(product_name='Microwave', brand='BrandC', product_description='700W', category=categories[2]),
]

sectors = [
    Sector(name='Warehouse A', location_description='First floor'),
    Sector(name='Warehouse B', location_description='Second floor'),
    Sector(name='Storefront', location_description='Main street'),
]

# Crear inventario con cantidades y fechas de expiración aleatorias
inventory_items = [
    Inventory(product=products[0], sector=sectors[0], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[1], sector=sectors[1], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[2], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
]

# Añadir categorías, productos, sectores e inventario a la sesión
session.add_all(categories)
session.add_all(products)
session.add_all(sectors)
session.add_all(inventory_items)

# Confirmar transacción
session.commit()

# Cerrar sesión
session.close()

print("Datos de prueba creados exitosamente")
