import tkinter as tk
from tkinter import ttk
from frames.frame_mixin import CenterWindowMixin
from config.database import Session
from services.product import ProductService
from schema.product import Product


class MainApplication(CenterWindowMixin):
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("300x200")

        # Inicializar la posición de la ventana
        self.window_position = None

        # Botones en la ventana principal
        btn_products = ttk.Button(root, text="Productos", command=self.open_products_window)
        # btn_boxes = ttk.Button(root, text="Ver Cajas", command=self.open_window2)
        # btn_warehouses = ttk.Button(root, text="Ver Almacenes", command=self.open_window2)
        # btn_stock = ttk.Button(root, text="Ver Inventario", command=self.open_window2)
        # btn3 = ttk.Button(root, text="Abrir Ventana 3", command=self.open_window3)

        btn_products.place(x=20,y=20)
        # btn_boxes.place(x=20,y=20)
        # btn_warehouses.place(x=20,y=20)
        # btn_stock.place(x=20,y=20)
        # btn2.pack(pady=10)
        # btn3.pack(pady=10)

        self.center_window(self.root)

    def open_products_window(self):
        ProductsWindow(self)

    # def open_window2(self):
    #     self.hide_main()
    #     Window2(self)

    # def open_window3(self):
    #     self.hide_main()
    #     Window3(self)

    def hide_main(self):
        # Guardar la posición de la ventana
        self.window_position = self.root.geometry()
        self.root.withdraw()

    def show_main(self):
        # Restaurar la posición de la ventana
        if self.window_position:
            self.root.geometry(self.window_position)
        self.root.deiconify()


class ProductsWindow(CenterWindowMixin):
    def __init__(self, main_app):
        self.main_app = main_app
        self.window = tk.Toplevel(main_app.root)
        self.window.title("Productos")
        self.window.geometry("1000x350")
        self.db = Session()

        self.product_service = ProductService(self.db)

        # Variables para los campos de entrada
        self.inpt_product_name = tk.StringVar()
        self.inpt_product_desc = tk.StringVar()
        self.inpt_product_cat = tk.StringVar()

        # Ingresar producto
        lbl_product_name = ttk.Label(self.window, text="Nombre de Producto")
        lbl_product_name.place(x=60,y=20)
        inpt_product_name = ttk.Entry(self.window, textvariable=self.inpt_product_name)
        inpt_product_name.place(x=60,y=40)

        lbl_product_desc = ttk.Label(self.window, text="Descripcion de Producto")
        lbl_product_desc.place(x=60,y=60)
        inpt_product_desc = ttk.Entry(self.window, textvariable=self.inpt_product_desc)
        inpt_product_desc.place(x=60,y=80)

        lbl_product_cat = ttk.Label(self.window, text="Categoria de Producto")
        lbl_product_cat.place(x=60,y=100)
        lbl_product_cat = ttk.Entry(self.window, textvariable=self.inpt_product_cat)
        lbl_product_cat.place(x=60,y=120)
        
        btn_insert = ttk.Button(self.window, text="Ingresar Producto", command=self.insert_product)
        btn_insert.place(x=90,y=150)

        btn_delete = ttk.Button(self.window, text="Eliminar Producto", command=self.delete_product)
        btn_delete.place(x=90,y=190)

        btn_close = ttk.Button(self.window, text="Cerrar Ventana", command=self.close_window)
        btn_close.place(x=850,y=300)

        # tabla 
        self.tree = ttk.Treeview(self.window, columns=("Id", "Nombre", "Descripcion","Categoria"), show="headings")
        # Definir los encabezados de la tabla
        self.tree.heading("Id", text="Id")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.heading("Categoria", text="Categoria")

        # Definir el tamaño de las columnas
        self.tree.column("Id", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Descripcion", width=300)
        self.tree.column("Categoria", width=150)

        # Empaquetar el Treeview en la ventana principal
        self.tree.place(x=300,y=20)

        self.load_products()

        self.center_window(self.window, main_app.root)

    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        products = self.product_service.get_products()
        for product in products:
            self.tree.insert("", tk.END, values=(product.id, product.product_name, product.product_description, product.category))


    def insert_product(self):
        nombre = self.inpt_product_name.get()
        descripcion = self.inpt_product_desc.get()
        categoria = self.inpt_product_cat.get()

        if nombre and descripcion and categoria:

            product_exist = self.product_service.get_product_by_name(nombre)
            if product_exist:
                print("error")
                return 
            product = Product(product_name=nombre, product_description=descripcion, category=categoria)
            self.product_service.create_product(product)
            self.load_products()

            self.inpt_product_name.set("")
            self.inpt_product_desc.set("")
            self.inpt_product_cat.set("")

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item)["values"][0]
            self.product_service.delete_product(product_id)
            self.load_products()

    def close_window(self):
        self.window_position = self.window.geometry()
        self.window.withdraw()
        # self.window.destroy()
        self.main_app.show_main()


# class Window2(CenterWindowMixin):
#     def __init__(self, main_app):
#         self.main_app = main_app
#         self.window = tk.Toplevel(main_app.root)
#         self.window.title("Ventana 2")
#         self.window.geometry("300x200")

#         btn_close = ttk.Button(self.window, text="Cerrar Ventana", command=self.close_window)
#         btn_close.pack(pady=20)

#         self.center_window(self.window, main_app.root)

#     def close_window(self):
#         self.window.destroy()
#         self.main_app.show_main()



# class Window3(CenterWindowMixin):
#     def __init__(self, main_app):
#         self.main_app = main_app
#         self.window = tk.Toplevel(main_app.root)
#         self.window.title("Ventana 3")
#         self.window.geometry("300x200")

#         btn_close = ttk.Button(self.window, text="Cerrar Ventana", command=self.close_window)
#         btn_close.pack(pady=20)

#         self.center_window(self.window, main_app.root)

#     def close_window(self):
#         self.window.destroy()
#         self.main_app.show_main()