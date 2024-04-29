import os
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup


# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
output_file = os.path.join(os.path.dirname(file), 'output.txt')

with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.readlines()

lines = []
html_string = ''
for tag in html_tags:
    if '<yt-pdg-comment-chip-renderer' in tag:
        lines.append(tag)

html_tags = '\n'.join(i for i in lines)

soup = BeautifulSoup(html_tags, 'html.parser')

# Encuentra todas las etiquetas `yt-attributed-string`
comments = soup.find_all("yt-attributed-string")

# Extrae el contenido de texto de cada etiqueta
textos = [comment.text for comment in comments]

for i in textos:
    print(i)

# Imprime el resultado
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(textos)
