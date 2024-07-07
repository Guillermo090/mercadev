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
    Product(product_name='Laptop', brand='BrandD', product_description='15-inch display', category=categories[0]),
    Product(product_name='Jeans', brand='BrandE', product_description='Denim', category=categories[1]),
    Product(product_name='Refrigerator', brand='BrandF', product_description='Energy efficient', category=categories[2]),
    Product(product_name='Headphones', brand='BrandG', product_description='Noise-cancelling', category=categories[0]),
    Product(product_name='Jacket', brand='BrandH', product_description='Waterproof', category=categories[1]),
    Product(product_name='Blender', brand='BrandI', product_description='500W', category=categories[2]),
    Product(product_name='Camera', brand='BrandJ', product_description='Digital SLR', category=categories[0]),
    Product(product_name='Tablet', brand='BrandK', product_description='10-inch display', category=categories[0]),
    Product(product_name='Dress', brand='BrandL', product_description='Summer style', category=categories[1]),
    Product(product_name='Oven', brand='BrandM', product_description='Electric oven', category=categories[2]),
    Product(product_name='Smartwatch', brand='BrandN', product_description='Fitness tracker', category=categories[0]),
    Product(product_name='Sweater', brand='BrandO', product_description='Woolen', category=categories[1]),
    Product(product_name='Vacuum Cleaner', brand='BrandP', product_description='High suction power', category=categories[2]),
    Product(product_name='Gaming Console', brand='BrandQ', product_description='Next-gen gaming', category=categories[0]),
    Product(product_name='Shorts', brand='BrandR', product_description='Comfort fit', category=categories[1]),
    Product(product_name='Dishwasher', brand='BrandS', product_description='Energy efficient', category=categories[2]),
    Product(product_name='Speaker', brand='BrandT', product_description='Bluetooth speaker', category=categories[0]),
    Product(product_name='Skirt', brand='BrandU', product_description='Casual wear', category=categories[1]),
    Product(product_name='Toaster', brand='BrandV', product_description='2-slice toaster', category=categories[2]),
    Product(product_name='Monitor', brand='BrandW', product_description='4K resolution', category=categories[0]),
    Product(product_name='Hat', brand='BrandX', product_description='Baseball cap', category=categories[1]),
    Product(product_name='Air Conditioner', brand='BrandY', product_description='Split AC', category=categories[2]),
    Product(product_name='Router', brand='BrandZ', product_description='Wi-Fi 6', category=categories[0]),
    Product(product_name='Socks', brand='BrandAA', product_description='Cotton blend', category=categories[1]),
    Product(product_name='Coffee Maker', brand='BrandBB', product_description='Automatic', category=categories[2]),
    Product(product_name='Printer', brand='BrandCC', product_description='Laser printer', category=categories[0]),
    Product(product_name='Scarf', brand='BrandDD', product_description='Woolen', category=categories[1]),
    Product(product_name='Fan', brand='BrandEE', product_description='Ceiling fan', category=categories[2]),
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
    Inventory(product=products[3], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[4], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[5], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[6], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[7], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[8], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[9], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[10], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[11], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[12], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[13], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[14], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[15], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[16], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[17], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[18], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[19], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[20], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[21], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[22], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[23], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[24], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[25], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[26], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[27], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
    Inventory(product=products[28], sector=sectors[2], quantity=random.randint(10, 100), expiration_date=date.today() + timedelta(days=random.randint(30, 365))),
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
