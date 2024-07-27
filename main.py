import tkinter as tk
import customtkinter as ctk
from frames.main_frame import MainApplication, InventoryWindow
from config.database import engine, Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    root = ctk.CTk()
    # ctk.set_appearance_mode('dark')
    # ctk.set_default_color_theme('green')
    app = InventoryWindow(root)
    # app.center_window(root)   
    root.mainloop()
