import os
import re
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import dir_access, json_query, date_str, export


# date = date_str()
json_file = dir_access('urls')
labels = json_query(json_file)['tiktok']

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

# Inspeccionamos el archivo
with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.read()

soup = BeautifulSoup(html_tags, "lxml")

a_values = []
for value in soup.find_all('a'):
    if (labels[0] in str(value)):
        a_values.append(value)

strong_values = []
for value in soup.find_all('strong'):
    if (labels[1] in str(value)):
        strong_values.append(value)

titles  = [str(item['title']) + '\n' for item in a_values]
views   = [item.text + '\n' for item in strong_values]
hrefs, hashtags, superhashtags = [], [], []
for item in a_values:
    links = re.findall(r'href="(.*?)"', str(item))
    hrefs.append(links[0])
    if len(links) > 1:
        hashtags.append(links[1:])
        superhashtags.extend(links[1:])
    else:
        hashtags.append('No tags')

info = {}
info['titles']      = titles
info['hrefs']       = hrefs
info['views']       = views
info['hashtags']    = hashtags

# Generamos los Reportes
user = hrefs[0].split('/')[3]
print(user)
for key in info.keys():
    print(f'{key}: {len(info[key])}')

output_file = os.path.join(os.path.dirname(file), f'{user}.txt')
supra_file  = os.path.join(os.path.dirname(file), f'{user}_hashtags.txt')
output_json = os.path.join(os.path.dirname(file), f'{user}.json')
output_xlsx = os.path.join(os.path.dirname(file), f'{user}.xlsx')

with open(output_file, 'w', encoding='utf-8') as f:
    for value in a_values:
        f.write(str(value) + '\n')

with open(supra_file, 'w', encoding='utf-8') as f:
    for item in list(set(superhashtags)):
        f.write(str(item) + '\n')

output_content = json.dumps(info, indent=4)
with open(output_json, 'w', encoding='utf-8') as f:
    f.writelines(output_content)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
