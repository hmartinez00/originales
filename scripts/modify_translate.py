import os
import json
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import analizar_srt
from sync_voice_over.ai_secure_query import process_command

# Abrir el archivo JSON
with open(r'settings\api\settings.json', 'r') as f:
    data = json.load(f)

# Configuramos la API KEY 
QUERY=data['queries']['synchronize']

root = tk.Tk()
root.withdraw()
# directory = filedialog.askdirectory()
file = filedialog.askopenfilename()
directory = os.path.dirname(file)
filename = os.path.basename(file)\
    .replace('.mp3', '')\
    .replace(' - copy.md', '')\
    .replace(' - traducido.srt', '')\
    .replace('.srt', '')\

# Ejemplo de uso
original_srt = os.path.join(directory, filename + '.srt')
traduccion_srt = os.path.join(directory, filename + ' - traducido.srt')
analizar_srt(original_srt, traduccion_srt)

ext = ' - traducido.srt'
final_ext = ' - modificado.srt'
command = QUERY
process_command(directory, ext, final_ext, command)
