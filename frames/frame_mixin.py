from screeninfo import get_monitors
import customtkinter as ctk
import datetime
from schema.product import Product, Inventory

class CenterWindowMixin:
    def center_window(self, window, parent=None):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()

        if parent:
            parent.update_idletasks()
            parent_geometry = self.get_geometry(parent)
            parent_x, parent_y, parent_width, parent_height = parent_geometry

            x = parent_x + (parent_width // 2) - (width // 2)
            y = parent_y + (parent_height // 2) - (height // 2)
        else:
            monitor = get_monitors()[0]  # Usar el monitor principal
            screen_width = monitor.width
            screen_height = monitor.height
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')

    @staticmethod
    def get_geometry(widget):
        """Get the geometry (x, y, width, height) of a widget."""
        return widget.winfo_x(), widget.winfo_y(), widget.winfo_width(), widget.winfo_height()
    
class MenuMixin:

    ALL_CATEGORIES = 'todos'


    def load_inventory(self):
        for row in self.parent_frame.tree.get_children():
            self.parent_frame.tree.delete(row)

        inventory_products = self.product_service.get_inventory_products()
        for inventory_product in inventory_products:
            self.parent_frame.tree.insert("", ctk.END, values=(
                inventory_product.id, 
                inventory_product.product_name,
                inventory_product.product_description,
                inventory_product.product_brand, 
                inventory_product.category_name, 
                inventory_product.quantity, 
                inventory_product.expiration_date))
            
    def load_categories(self):

        all_categories = [self.ALL_CATEGORIES]
        categories = all_categories +  [ str(cat.category_name) for cat in self.product_service.get_categories()]
        self.parent_frame.inpt_product_cat_search.configure(values=categories)

    def close_window(self):
        self.window_position = self.parent_frame.geometry()
        self.parent_frame.destroy()

    def search_inventory(self):
        for row in self.parent_frame.tree.get_children():
            self.parent_frame.tree.delete(row)

        searched_category = self.parent_frame.inpt_product_cat_search.get()
        if searched_category == MenuMixin.ALL_CATEGORIES:
            searched_category = ""

        inventory_products = self.product_service.get_inventory_with_filters(
            searched_name = self.inpt_product_name_search.get(),
            searched_desc = self.inpt_product_desc_search.get(),
            searched_brand = self.inpt_product_brand_search.get(),
            searched_cat = searched_category
        )

        for inventory_product in inventory_products:
            self.parent_frame.tree.insert("", ctk.END, values=(
                inventory_product.id, 
                inventory_product.product_name,
                inventory_product.product_description,
                inventory_product.product_brand, 
                inventory_product.category_name, 
                inventory_product.quantity, 
                inventory_product.expiration_date))

    def insert_product(self):
        nombre = self.inpt_product_name.get()
        descripcion = self.inpt_product_desc.get()
        brand = self.inpt_product_brand.get()
        category_name = self.inpt_product_cat.get()
        quantity = self.inpt_product_quantity.get()
        expiration_date = self.inpt_product_expiration_date.get()

        if nombre :
            product_exist = self.product_service.get_product_by_name(nombre)
            if product_exist:
                print("producto ya existe")
                return 
            
            category = self.product_service.get_or_create_category(category_name)
            sector = self.product_service.get_or_create_sector("Casa")

            product_schema = Product(product_name=nombre, product_description=descripcion, brand=brand, category_id=category.id)
            new_product = self.product_service.create_product(product_schema)

            expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)

            inventory_schema = Inventory(product_id=new_product.id, quantity=int(quantity),sector_id=sector.id,expiration_date=expiration_date)
            self.product_service.create_inventory(inventory_schema)

            self.load_inventory()

            self.load_categories()  

            self.inpt_product_name.set("")
            self.inpt_product_desc.set("")
            self.inpt_product_brand.set("")
            self.inpt_product_cat.set("")
            self.inpt_product_quantity.set("")
            self.inpt_product_expiration_date.set("")
 
    def delete_product(self):
        selected_item = self.parent_frame.tree.selection()
        if selected_item:
            inventory_id = self.parent_frame.tree.item(selected_item)["values"][0]
            # self.product_service.delete_product(product_id)
            self.product_service.delete_inventory(inventory_id)
            # self.load_products()
            self.load_inventory()
            self.load_categories()  