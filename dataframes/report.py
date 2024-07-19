import pandas as pd
import os
import sys
import datetime
from sqlalchemy.orm import Session

# Añadir el directorio raíz al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from config.database import engine
from models.product import Product as ProductModel, Inventory as InventoryModel, Category as CategoryModel,  Sector as SectorModel
from schema.product import Product, Category
from services.product import ProductService  # Asegúrate de que la ruta sea correcta



class InventoryDataFrame:

    def __init__(self, db: Session):
        self.product_service = ProductService(db)

    def get_inventory_products(self):

        # Obtener los datos del inventario
        inventory_data = self.product_service.get_inventory_products()

        # Convertir los datos a un DataFrame de pandas
        df = pd.DataFrame([{
            'id': item.id,
            'quantity': item.quantity,
            'expiration_date': item.expiration_date,
            'created_at': item.created_at,
            'sector_name': item.sector_name,
            'sector_description': item.sector_description,
            'category_name': item.category_name,
            'product_name': item.product_name,
            'product_description': item.product_description,
            'product_brand': item.product_brand
        } for item in inventory_data])

        today = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
        # Guardar los datos en un archivo Excel
        df.to_excel(f'respaldos/inventory_data_{today}.xlsx', index=False)

        print("Datos exportados a inventory_data.xlsx con éxito")