import os
import shutil
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files


# Crear una ventana de diálogo
root = tk.Tk()
root.withdraw()

# Abrir un explorador de archivos para seleccionar una carpeta
# Acá hay que seleccionar la carpeta de traducidos!
folder_path = filedialog.askdirectory()

# Crear una carpeta dentro del directorio: traducidos
procesess_dir = os.path.join(folder_path, "sincronizar")
os.makedirs(
    procesess_dir,
    exist_ok=True
)

# Buscamos los archivos dentro del directorio
extensions = ['traducido.srt', '.mp4']
files = []
for ext in extensions:
    files.extend(find_files(folder_path, ext))

print(files)

# Moviendo archivos
for file in files:
    filename = os.path.basename(file)
    shutil.move(file, os.path.join(procesess_dir, filename))

