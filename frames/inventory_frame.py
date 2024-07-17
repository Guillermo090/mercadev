import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from frames.frame_mixin import CenterWindowMixin
from config.database import Session
from services.product import ProductService
from schema.product import Product, Inventory

class InventoryWindow(CenterWindowMixin):
    def __init__(self, main_app):
        self.main_app = main_app
        # self.window = tk.Toplevel(main_app.root)
        self.window = ctk.CTkToplevel(main_app.root)
        self.window.title("Productos")
        self.window.geometry("1550x650")
        self.db = Session()

        self.product_service = ProductService(self.db)

        frame = ctk.CTkFrame(self.window, fg_color="#FF99FF",width=250,height=650, corner_radius=0)
        frame.place(x=0, y=0 )
        frame2 = ctk.CTkFrame(self.window, fg_color="#FFCCFF",width=1300,height=650, corner_radius=0)
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

        btn_close = ttk.Button(frame2, text="Cerrar Ventana", command=self.close_window)
        btn_close.place(x=1000,y=550)

        bnt_inv = ttk.Button(self.window, text="Cargar inventario", command=self.load_inventory)
        bnt_inv.place(x=550,y=300)

        # frame_search = ctk.CTkFrame(self.window, fg_color="#FF99FF",width=250,height=650, corner_radius=0)
        # frame_search.place(x=0, y=0 )

        # tabla 
        self.tree = ttk.Treeview(self.window, columns=("Id", "Nombre", "Descripcion","Marca","Categoria","Cantidad","Vencimiento"), show="headings")
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
        self.tree.place(x=275,y=160, width=1250)

        self.load_inventory()

        self.center_window(self.window, main_app.root)

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
        self.window_position = self.window.geometry()
        self.window.withdraw()
        # self.window.destroy()
        self.main_app.show_main()