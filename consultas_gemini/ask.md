```
import tkinter as tk
from tkinter import filedialog

# Crear una ventana de diálogo
root = tk.Tk()
root.withdraw()

# Abrir un explorador de archivos para seleccionar una carpeta
folder_path = filedialog.askdirectory()

# Obtener la ruta de la carpeta seleccionada
if folder_path:
    print("Ruta de la carpeta seleccionada:", folder_path)
else:
    print("No se seleccionó ninguna carpeta.")

# Cerrar la ventana de diálogo
root.destroy()
```