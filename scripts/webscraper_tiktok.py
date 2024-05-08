import os
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import dir_access, json_query, date_str, export


def only_value(soup, input_list):
    import re

    option = input_list[0]
    tag = input_list[1]
    attr = input_list[2]
    line_label = input_list[3]
    pattern = input_list[4]

    list_values  = []
    for value in soup.find_all(tag):
        if (line_label in str(value)):
            if pattern == None:
                if attr != 'text':
                    item = str(value[attr]) + '\n'
                else:
                    item = value.text + '\n'
            else:
                item = re.findall(pattern, str(value))
            
            if option == 'app':
                list_values.append(item)
            elif option == 'ext':
                list_values.extend(item)

    return list_values

# json_file = dir_access('urls')
# labels = dict(json_query(json_file)['tiktok'])

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

# Inspeccionamos el archivo
with open(file, 'r', encoding='utf-8') as f:
    html_tags = f.read()

soup = BeautifulSoup(html_tags, "lxml")

dict_1 = {
    'titles'      :['app', 'a', 'title', 'title=', None],
    'views'       :['app', 'strong', 'text', 'data-e2e="video-views"', None],
    'hrefs'       :['app', 'a', 'href', 'title=', None],
    'hashtags'    :['app', 'a', None, 'title=', r'href="(.*?)"'],
    's_hashtags'  :['ext', 'a', None, 'title=', r'href="(.*?)"'],
}

titles      = only_value(soup, dict_1['titles'])
views       = only_value(soup, dict_1['views'])
hrefs       = only_value(soup, dict_1['hrefs'])
hashtags    = only_value(soup, dict_1['hashtags'])
s_hashtags  = only_value(soup, dict_1['s_hashtags'])

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
    for value in soup.find_all('a'):
        f.write(str(value) + '\n')

with open(supra_file, 'w', encoding='utf-8') as f:
    for item in list(set(s_hashtags)):
        f.write(str(item) + '\n')

output_content = json.dumps(info, indent=4)
with open(output_json, 'w', encoding='utf-8') as f:
    f.writelines(output_content)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
