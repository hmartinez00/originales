import tkinter as tk
from tkinter import filedialog
import mutagen.mp3

root = tk.Tk()
root.withdraw()

# Abrir el explorador de archivos y permitir la selección de un archivo
audio_url = filedialog.askopenfilename()

# Obtener el archivo MP3
audio = mutagen.mp3.MP3(audio_url)

# Obtener la duración en segundos
duracion = round(audio.info.length)

# Imprimir la duración
print(f"Duration (s): {duracion}")