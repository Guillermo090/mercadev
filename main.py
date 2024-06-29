import tkinter as tk
from frames.main_frame import MainApplication
from config.database import engine, Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    root = tk.Tk()
    app = MainApplication(root)
    app.center_window(root)  # Center the main window as well
    root.mainloop()
