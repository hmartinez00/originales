import os
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.module_extractor import html_format, extract_values_tag

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
tag = 'a'

output_file = os.path.join(os.path.dirname(file), 'output.txt')

# Extract values content after interacting with elements
# html_content = html_format(file)

# Leer el código HTML desde un archivo
with open(file, "r", encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
values = soup.find_all(tag)
content = []
# Iterar sobre las etiquetas 'a' y obtener el título
for etiqueta_a in values:
    titulo = etiqueta_a.get('title')
    if titulo:
        content.append(f'{titulo}\n')

print(len(content))
# Guardando valores
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(content)
