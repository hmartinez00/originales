import os
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import dir_access, json_query, date_str, export
from sync_voice_over.module_extractor import html_format, extract_html_values_tag


# date = date_str()
# json_file = dir_access('urls')
# labels = json_query(json_file)['tiktok']

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()
output_file = os.path.join(os.path.dirname(file), 'output.txt')
output_json = os.path.join(os.path.dirname(file), 'output.json')
output_xlsx = os.path.join(os.path.dirname(file), 'output.xlsx')

with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.read()

soup = BeautifulSoup(html_tags, "lxml")
a_values = [value for value in soup.find_all('a') if 'title=' in str(value)]
strong_values = [value for value in soup.find_all('strong') if 'data-e2e="video-views"' in str(value)]

titles = [str(item['title']) + '\n' for item in a_values]
hrefs  = [str(item['href']) + '\n' for item in a_values]
views  = [item.text + '\n' for item in strong_values]

info = {}
info['titles']  = titles
info['hrefs']   = hrefs
info['views']   = views

for key in info.keys():
    print(f'{key}: {len(info[key])}')

with open(output_file, 'w', encoding='utf-8') as f:
    for value in a_values:
        f.write(str(value) + '\n')

output_content = json.dumps(info, indent=4)
with open(output_json, 'w', encoding='utf-8') as f:
    f.writelines(output_content)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
