# Mercadev

**Mercadev** es un sistema de administración de mercadería diseñado para gestionar eficientemente inventarios y procesos relacionados con la gestión de productos.

## Características

- **Gestión de inventario:** Monitorea y controla el stock de productos en tiempo real.
- **Integración de datos:** Utiliza `pandas` y `SQLAlchemy` para manipulación y almacenamiento de datos.
- **Interfaz de usuario:** Construida con `customtkinter` para una experiencia amigable.
- **Exportación de datos:** Soporta la exportación de datos a formatos comunes como Excel.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Guillermo090/mercadev.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el script para crear la base de datos:
   ```bash
   python create_db.py
   ```

## Uso

Para iniciar el sistema, ejecuta:
```bash
python main.py
```

## Estructura del Proyecto

- **`config/`**: Configuraciones del proyecto.
- **`dataframes/`**: Manejo de los dataframes utilizados en el sistema.
- **`models/`**: Definición de modelos de datos.
- **`services/`**: Servicios utilizados en la aplicación.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo la Licencia MIT.

## Comando para generar ejecutable

```
pyinstaller --onefile --noconsole --add-data "mercadev.sqlite;." --hidden-import altgraph --hidden-import annotated-types --hidden-import customtkinter --hidden-import cx_Freeze --hidden-import cx_Logging --hidden-import darkdetect --hidden-import et-xmlfile --hidden-import greenlet --hidden-import lief --hidden-import numpy --hidden-import openpyxl --hidden-import packaging --hidden-import pandas --hidden-import pefile --hidden-import pydantic --hidden-import pydantic_core --hidden-import pyinstaller-hooks-contrib --hidden-import python-dateutil --hidden-import pytz --hidden-import pywin32-ctypes --hidden-import screeninfo --hidden-import setuptools --hidden-import six --hidden-import SQLAlchemy --hidden-import typing_extensions --hidden-import tzdata --hidden-import wheel main.py
```