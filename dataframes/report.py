import pandas as pd
import os
import sys
import datetime
from sqlalchemy.orm import Session
from services.product import ProductService  # Asegúrate de que la ruta sea correcta
from openpyxl.styles import Alignment

# Añadir el directorio raíz al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

class InventoryDataFrame:

    def __init__(self, db: Session):
        self.product_service = ProductService(db)

    def get_inventory_products(self):

        # Obtener los datos del inventario
        inventory_data = self.product_service.get_inventory_products()

        # Convertir los datos a un DataFrame de pandas
        df = pd.DataFrame([{
            'ID': item.id,
            'Nombre': item.product_name,
            'Descripcion': item.product_description,
            'Cantidad': item.quantity,
            'Fecha de Creación': item.created_at.strftime('%d-%m-%Y %H:%M'),
            'Fecha de Vencimiento': item.expiration_date.strftime('%d-%m-%Y'),
            'Marca': item.product_brand,
            'Categoría': item.category_name,
            'Sector': item.sector_name,
        } for item in inventory_data])

        today = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
        filename = f'respaldos/inventory_data_{today}.xlsx'

        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

            # Obtener la hoja de trabajo y ajustar anchos de las columnas
            worksheet = writer.sheets['Sheet1']
            worksheet.column_dimensions['B'].width = 25  # Columna ID
            worksheet.column_dimensions['C'].width = 35  # Columna ID
            worksheet.column_dimensions['D'].width = 15  # Columna Cantidad
            worksheet.column_dimensions['E'].width = 20  # Columna Cantidad
            worksheet.column_dimensions['F'].width = 20  # Columna Cantidad
            worksheet.column_dimensions['G'].width = 25  # Columna Marca
            worksheet.column_dimensions['H'].width = 25  # Columna Categoría

        # Centrar el contenido de columnas específicas
        center_alignment = Alignment(horizontal='center')

        # Aplicar la alineación a cada celda en el rango que contiene datos y títulos
        for row in worksheet.iter_rows(min_row=1, max_row=worksheet.max_row, min_col=1, max_col=9):
            for cell in row:
                cell.alignment = center_alignment

        print("Datos exportados a inventory_data.xlsx con éxito")