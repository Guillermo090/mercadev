import tkinter as tk
from tkinter import ttk
from frames.frame_mixin import CenterWindowMixin
from config.database import Session
from services.product import ProductService
from schema.product import Product
from frames.inventory_frame import InventoryWindow


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
        InventoryWindow(self)

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