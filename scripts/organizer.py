import os
import shutil
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files


root = tk.Tk()
root.withdraw()

# Abrir el explorador de archivos y permitir la selección de un archivo
video_url = filedialog.askopenfilename()

# Obtener la ruta del directorio donde se encuentra el video
# y nombre del mismo
video_dir = os.path.dirname(video_url)
video_name = os.path.basename(video_url).split(".")[0].replace(' ', '_')

# Crear una carpeta dentro del directorio del video
procesess_dir = os.path.join(video_dir, "procesados")
os.makedirs(
    os.path.join(procesess_dir, video_name),
    exist_ok=True
)

extensiones = [
    '.mp3',
    '.srt',
    # 'traducido.srt',
    'copy.md',
]

# Buscando archivos
files = []
for ext in extensiones:
    # print(ext)
    lista = find_files(video_dir, ext)
    files.extend(lista)

# Moviendo archivos
shutil.move(video_url, os.path.join(procesess_dir, video_name, video_name + '.mp4'))
for file in files:
    # Comprobar si el título del archivo contiene el título del video
    if video_name in file:
        file_name = os.path.basename(file)
        print(video_name, file, (video_name in file))
        # Mover el archivo a la carpeta de procesados
        shutil.move(file, os.path.join(procesess_dir, video_name ,file_name))