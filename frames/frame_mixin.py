from screeninfo import get_monitors

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