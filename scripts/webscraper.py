import os
import json
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup


label_user      = '              @'
label_comment   = '<yt-pdg-comment-chip-renderer'

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
output_file = os.path.join(os.path.dirname(file), 'output.json')

with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.readlines()

users = []
lines = []
html_string = ''
for tag in html_tags:
    if label_user in tag:
        users.append(tag.replace(label_user, '').replace('\n', ''))
    if label_comment in tag:
        lines.append(tag)

print(len(users))

html_tags = '\n'.join(i for i in lines)

soup = BeautifulSoup(html_tags, 'html.parser')

# Encuentra todas las etiquetas `yt-attributed-string`
comments = soup.find_all("yt-attributed-string")

# Extrae el contenido de texto de cada etiqueta
textos = [comment.text for comment in comments]

# Imprime el resultado
json_dict = {}
for i, key in enumerate(users):
    value = textos[i]
    json_dict[key] = value

output_content = json.dumps(json_dict, indent=4)
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(output_content)
