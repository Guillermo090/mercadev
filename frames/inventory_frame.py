import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from frames.frame_mixin import CenterWindowMixin
from config.database import Session
from services.product import ProductService
from schema.product import Product, Inventory
from dataframes.report import InventoryDataFrame

class InventoryWindow(CenterWindowMixin):
    def __init__(self, main_app):
        self.main_app = main_app
        # self.window = tk.Toplevel(main_app.root)
        self.main_app = self.main_app
        self.main_app.title("Productos")
        self.main_app.geometry("1550x650")
        self.db = Session()


        self.product_service = ProductService(self.db)

        frame = ctk.CTkFrame(self.main_app, fg_color="#FF99FF",width=250,height=650, corner_radius=0)
        frame.place(x=0, y=0 )
        frame2 = ctk.CTkFrame(self.main_app, fg_color="#FFCCFF",width=1300,height=650, corner_radius=0)
        frame2.place(x=250, y=0 )

        # Variables para los campos de entrada
        self.inpt_product_name = tk.StringVar()
        self.inpt_product_desc = tk.StringVar()
        self.inpt_product_brand = tk.StringVar()
        self.inpt_product_cat = tk.StringVar()
        self.inpt_product_quantity = tk.StringVar()
        self.inpt_product_expiration_date = tk.StringVar()

        # Ingresar producto
        # lbl_product_name = ttk.Label(frame, text="Nombre del Producto")
        lbl_product_name = ctk.CTkLabel(frame, text="Nombre del Producto",text_color="#990066")
        lbl_product_name.place(x=60,y=10)
        # inpt_product_name = ttk.Entry(frame, textvariable=self.inpt_product_name)
        inpt_product_name = ctk.CTkEntry(frame, textvariable=self.inpt_product_name)
        inpt_product_name.place(x=60,y=30)

        lbl_product_desc = ctk.CTkLabel(frame, text="Descripcion",text_color="#990066")
        lbl_product_desc.place(x=60,y=60)
        inpt_product_desc = ctk.CTkEntry(frame, textvariable=self.inpt_product_desc)
        inpt_product_desc.place(x=60,y=80)

        lbl_product_brand = ctk.CTkLabel(frame, text="Marca",text_color="#990066")
        lbl_product_brand.place(x=60,y=110)
        lbl_product_brand = ctk.CTkEntry(frame, textvariable=self.inpt_product_brand)
        lbl_product_brand.place(x=60,y=130)

        lbl_product_cat = ctk.CTkLabel(frame, text="Categoria",text_color="#990066")
        lbl_product_cat.place(x=60,y=160)
        inpt_product_cat = ctk.CTkEntry(frame, textvariable=self.inpt_product_cat)
        inpt_product_cat.place(x=60,y=180)

        lbl_product_qty = ctk.CTkLabel(frame, text="Cantidad",text_color="#990066")
        lbl_product_qty.place(x=60,y=210)
        inpt_product_qty = ctk.CTkEntry(frame, textvariable=self.inpt_product_quantity)
        inpt_product_qty.place(x=60,y=230)

        lbl_product_expiration = ctk.CTkLabel(frame, text="Fecha Fencimiento",text_color="#990066")
        lbl_product_expiration.place(x=60,y=260)
        inpt_product_expiration = ctk.CTkEntry(frame, textvariable=self.inpt_product_expiration_date)
        inpt_product_expiration.place(x=60,y=280)
        
        btn_insert = ctk.CTkButton(frame, text="Ingresar", command=self.insert_product, width=65)
        btn_insert.place(x=50,y=320)

        btn_delete = ctk.CTkButton(frame, text="Eliminar", command=self.delete_product, width=65)
        btn_delete.place(x=150,y=320)

        btn_close = ctk.CTkButton(frame2, text="Cerrar Ventana", command=self.close_window, width=65)
        btn_close.place(x=1150,y=575)


        inv_df = InventoryDataFrame(self.db)

        bnt_inv = ctk.CTkButton(frame2, text="Cargar Respaldo", command=inv_df.get_inventory_products, width=65)
        bnt_inv.place(x=1000,y=575)

        frame_search = ctk.CTkFrame(frame2, fg_color="#FF99FF",width=1000,height=50, corner_radius=30)
        frame_search.place(x=150, y=25 )

        # Variables para los campos de entrada
        self.inpt_product_name_search = tk.StringVar()
        self.inpt_product_desc_search = tk.StringVar()
        self.inpt_product_brand_search = tk.StringVar()
        self.inpt_product_cat_search_var = tk.StringVar()

        lbl_product_name_search = ctk.CTkLabel(frame_search, text="Nombre",text_color="#990066")
        lbl_product_name_search.place(x=25,y=10)
        inpt_product_name_search = ctk.CTkEntry(frame_search, textvariable=self.inpt_product_name_search)
        inpt_product_name_search.place(x=75 ,y=10)

        lbl_product_desc_search = ctk.CTkLabel(frame_search, text="Descripcion",text_color="#990066")
        lbl_product_desc_search.place(x=250,y=10)
        inpt_product_desc_search = ctk.CTkEntry(frame_search, textvariable=self.inpt_product_desc_search)
        inpt_product_desc_search.place(x=325,y=10)

        lbl_product_brand_search = ctk.CTkLabel(frame_search, text="Marca",text_color="#990066")
        lbl_product_brand_search.place(x=490,y=10)
        inpt_product_brand_search = ctk.CTkEntry(frame_search, textvariable=self.inpt_product_brand_search)
        inpt_product_brand_search.place(x=530,y=10)

        categories = [ str(cat.category_name) for cat in self.product_service.get_categories()]

        lbl_product_cat_search = ctk.CTkLabel(frame_search, text="Categoria",text_color="#990066")
        lbl_product_cat_search.place(x=700,y=10)
        self.inpt_product_cat_search = ctk.CTkComboBox(frame_search, values=categories )
        self.inpt_product_cat_search.place(x=760,y=10)

        bnt_inv = ctk.CTkButton(frame_search, text="Buscar", width=65, command=self.search_inventory)
        bnt_inv.place(x=915,y=10)

        # tabla 
        self.tree = ttk.Treeview(self.main_app, columns=("Id", "Nombre", "Descripcion","Marca","Categoria","Cantidad","Vencimiento"), show="headings")
        # Definir los encabezados de la tabla
        self.tree.heading("Id", text="Id")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Vencimiento", text="Vencimiento")

        # Definir el tamaño de las columnas
        self.tree.column("Id", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Descripcion", width=150)
        self.tree.column("Marca", width=85)
        self.tree.column("Categoria", width=95)
        self.tree.column("Cantidad", width=50)
        self.tree.column("Vencimiento", width=150)

        # Empaquetar el Treeview en la ventana principal
        self.tree.place(x=275,y=100, width=1250,height=450)

        self.load_inventory()

        # self.center_window(self.main_app, main_app.root)

        style = ttk.Style()
        style.theme_use("default")
        # Estilo general del Treeview
        style.configure("Treeview",
            background="#FF99FF",
            foreground="#990066",
            rowheight=25,
            fieldbackground="#D3D3D3",
            font=("Helvetica", 10)
        )

        # Estilo para el encabezado
        style.configure("Treeview.Heading",
                        background="#FF99FF",
                        foreground="#990066",
                        font=("Helvetica", 12, "bold"))

        # Cambiar el color de la fila seleccionada
        style.map("Treeview", background=[("selected", "#347083")])


    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        inventory_products = self.product_service.get_inventory_products()
        for inventory_product in inventory_products:
            self.tree.insert("", tk.END, values=(
                inventory_product.id, 
                inventory_product.product_name,
                inventory_product.product_description,
                inventory_product.product_brand, 
                inventory_product.category_name, 
                inventory_product.quantity, 
                inventory_product.expiration_date))

    def load_inventory(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        inventory_products = self.product_service.get_inventory_products()
        for inventory_product in inventory_products:
            self.tree.insert("", tk.END, values=(
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

            product_schema = Product(product_name=nombre, brand=brand, category_id=category.id)
            new_product = self.product_service.create_product(product_schema)

            inventory_schema = Inventory(product_id=new_product.id, quantity=int(quantity),sector_id=1,expiration_date='2021-01-01')
            self.product_service.create_inventory(inventory_schema)


            self.load_inventory()

            self.inpt_product_name.set("")
            self.inpt_product_desc.set("")
            self.inpt_product_brand.set("")
            self.inpt_product_cat.set("")
            self.inpt_product_quantity.set("")
            self.inpt_product_expiration_date.set("")

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            inventory_id = self.tree.item(selected_item)["values"][0]
            # self.product_service.delete_product(product_id)
            self.product_service.delete_inventory(inventory_id)
            # self.load_products()
            self.load_inventory()

    def close_window(self):
        self.window_position = self.main_app.geometry()
        self.main_app.destroy()

    
    def search_inventory(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        print(self.inpt_product_cat_search_var)

        inventory_products = self.product_service.get_inventory_with_filters(
            searched_name = self.inpt_product_name_search.get(),
            searched_desc = self.inpt_product_desc_search.get(),
            searched_brand = self.inpt_product_brand_search.get(),
            searched_cat = self.inpt_product_cat_search.get()
        )
        for inventory_product in inventory_products:
            self.tree.insert("", tk.END, values=(
                inventory_product.id, 
                inventory_product.product_name,
                inventory_product.product_description,
                inventory_product.product_brand, 
                inventory_product.category_name, 
                inventory_product.quantity, 
                inventory_product.expiration_date))