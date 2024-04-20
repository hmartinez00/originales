# Importamos Gemini Pro, textwrap, IPython, sys, para soporte Para Caracteres Especiales en la Terminal de Python 
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.ai_secure_query import process_command


# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

ext1 = '.srt'
final_ext1 = ' - traducido.srt'
command1 = 'Traduce el siguiente archivo de subtitulos al castellano. Entrega el resultado en formato de archivo srt con las misma marcas de tiempo que ya tiene.'
process_command(directory, ext1, final_ext1, command1)
