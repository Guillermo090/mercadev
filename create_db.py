from config.database import engine, Base
from schema.product import Product, Category  # Asegúrate de importar tus modelos

if __name__ == "__main__":
    print("Creando la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada correctamente.")