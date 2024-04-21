import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import move_batch

root = tk.Tk()
root.withdraw()

# Abrir el explorador de archivos y permitir la selección de un archivo
file_url = filedialog.askopenfilename()
# Abrir el explorador de archivos y permitir la selección de un directorio
directory = filedialog.askdirectory()

move_batch(file_url, directory)