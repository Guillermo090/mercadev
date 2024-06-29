from models.product import Product as ProductModel
from schema.product import Product


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
        return True


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
    
