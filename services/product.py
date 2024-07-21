from models.product import Product as ProductModel, Inventory as InventoryModel, Category as CategoryModel,  Sector as SectorModel
from schema.product import Product, Category
from sqlalchemy.orm import aliased

class ProductService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_products(self):
        return self.db.query(ProductModel).all()
        
    def get_product(self, id):
        return self.db.query(ProductModel).filter(ProductModel.id == id).first()
    
    def get_product_by_name(self, product_name):
        return self.db.query(ProductModel).filter(ProductModel.product_name == product_name).first()

    def create_product(self, product: Product):
        new_product = ProductModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()
        return new_product

    def update_product(self, id: int, data: Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if product:
            product.product_name = data.product_name 
            product.product_description = data.product_description 
            product.category = data.category 
            self.db.commit()
            return True
        return False

    def delete_product(self, id: int):
       self.db.query(ProductModel).filter(ProductModel.id == id).delete()
       self.db.commit()
       return True
    
    def get_inventory_products(self):

        # Alias para las tablas para facilitar la consulta
        product_alias = aliased(ProductModel)
        category_alias = aliased(CategoryModel)
        sector_alias = aliased(SectorModel)

        return self.db.query(
            InventoryModel.id,
            InventoryModel.quantity,
            InventoryModel.expiration_date,
            InventoryModel.created_at,
            sector_alias.name.label('sector_name'),
            sector_alias.location_description.label('sector_description'),
            category_alias.category_name.label('category_name'),
            product_alias.product_name.label('product_name'),
            product_alias.product_description.label('product_description'),
            product_alias.brand.label('product_brand')
        ).join(product_alias, InventoryModel.product).join(sector_alias, InventoryModel.sector).join(category_alias, product_alias.category).all()
    
    def get_categories(self):
        return self.db.query(CategoryModel.category_name).all()

    def get_or_create_category(self, category_name):

        category = self.db.query(CategoryModel).filter(CategoryModel.category_name == category_name).first()
        if not category:
            category_schema = Category(category_name=category_name)
            category = CategoryModel(**category_schema.model_dump())
            self.db.add(category)
            self.db.commit()
        return category
            
    def create_inventory(self, inventory):
        
        new_inventory = InventoryModel(**inventory.model_dump())
        self.db.add(new_inventory)
        self.db.commit()
        return new_inventory
    

    def delete_inventory(self, id: int):
        
        inventory = self.db.query(InventoryModel).filter(InventoryModel.id == id).first()
        if inventory:
            inventory_deleted = self.db.query(InventoryModel).filter(InventoryModel.id == id).delete()
            product_id = inventory.product_id
            self.delete_product(product_id)
            self.db.commit()
            return True
        return False