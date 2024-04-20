# Importamos Gemini Pro, textwrap, IPython, sys, para soporte Para Caracteres Especiales en la Terminal de Python 
import json
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.ai_secure_query import process_command

# Abrir el archivo JSON
with open(r'settings\api\settings.json', 'r') as f:
    data = json.load(f)

# Configuramos la API KEY 
QUERY=data['queries']['copies']

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

ext2 = ' - traducido.srt'
final_ext2 = ' - copy.md'
command2 = QUERY
process_command(directory, ext2, final_ext2, command2)
