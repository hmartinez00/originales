import os
import shutil
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_all_files


root = tk.Tk()
root.withdraw()

# Abrir el explorador de archivos y permitir la selección de un archivo
video_url = filedialog.askopenfilename()

# Obtener la ruta del directorio donde se encuentra el video
# y nombre del mismo
video_dir = os.path.dirname(video_url)
video_name = os.path.basename(video_url).replace(' - traducido.mp4', '')
base_dir = os.path.dirname(video_dir)

# Buscando archivos
# files = os.listdir(video_dir)
extensiones = [
    '.mp3',
    '.mp4',
    '.srt',
]

# Buscando archivos
files = find_all_files(video_dir, extensiones)

for file in files:
    # Comprobar si el título del archivo contiene el título del video
    if video_name in file:
        new_dir = os.path.join(base_dir, video_name)
        new_file = os.path.join(new_dir, os.path.basename(file))
        print(file, new_file)
        shutil.move(file, new_file)
