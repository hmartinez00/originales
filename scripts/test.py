import os
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import dir_access, json_query, date_str, export


date = date_str()

json_file = dir_access('urls')
labels = json_query(json_file)['youtube']

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
output_file = os.path.join(os.path.dirname(file), f'output_{date}.json')
output_xlsx = os.path.join(os.path.dirname(file), f'output_{date}.xlsx')

with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.readlines()

info = {}
for label in labels:
    list_values = []
    for tag in html_tags:
        if label in tag:
            # Extrae el texto de cada objeto BeautifulSoup
            list_values.append(BeautifulSoup(tag, "html.parser"))
    texts = [soup.text for soup in list_values]
    info[label] = texts

for key in info.keys():
    print(f'{key}: {len(info[key])}')

output_content = json.dumps(info, indent=4)
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(output_content)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
