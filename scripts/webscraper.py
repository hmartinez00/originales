import os
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import export


label_user      = '              @'
label_comment   = '<yt-pdg-comment-chip-renderer'

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
output_file = os.path.join(os.path.dirname(file), 'output.json')
output_users = os.path.join(os.path.dirname(file), 'output_users.txt')
output_textos = os.path.join(os.path.dirname(file), 'output_textos.txt')

with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.readlines()

users = []
lines = []
html_string = ''
for tag in html_tags:
    if label_user in tag:
        users.append(tag.replace(label_user, ''))
    if label_comment in tag:
        lines.append(tag)

print(len(users), len(lines))

# Crea un objeto BeautifulSoup para cada línea
soup_list = []
for line in lines:
    soup_list.append(BeautifulSoup(line, "html.parser"))

# Extrae el texto de cada objeto BeautifulSoup
texts = [soup.text for soup in soup_list]

# Imprime los textos extraídos
# print(texts)

# Guardando usuarios
with open(output_users, 'w', encoding='utf-8') as f:
    f.writelines(users)

# Guardando valores
with open(output_textos, 'w', encoding='utf-8') as f:
    f.writelines(texts)

# Imprime el resultado
json_dict = {}
for i, key in enumerate(users):
    value = texts[i]
    json_dict[str(key).replace('\n', '')] = value

output_content = json.dumps(json_dict, indent=4)
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(output_content)

output_xlsx = os.path.join(os.path.dirname(file), 'output.xlsx')
df = pd.DataFrame.from_dict(json_dict, orient='index')
df.columns = ["Texto"]
df.reset_index(inplace=True)
df.rename(columns={"index": "Usuario"}, inplace=True)
print(df)
export(df, output_xlsx)
