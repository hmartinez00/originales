import tkinter as tk
from tkinter import filedialog
import pandas as pd
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import export

id = "CardPc_titleText__RYOWo"

# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

# Inspeccionamos el archivo
with open(file, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
tags = soup.find_all('span')

info = {}
hashtags, posts, views = [], [], []
for tag in range(len(tags)):
    if id in str(tags[tag]):
        hashtags.append(str(tags[tag + 0].text) + '\n')
        print(str(tags[tag + 0].text))
        ticket = []
        i = 1
        while len(ticket) < 2:
            if 'Posts' in str(tags[tag + i].text):
                value = int(str(tags[tag + i - 1].text).replace('K', ''))*1000
                posts.append(value)
                ticket.append(True)
                print(len(ticket), value)
                i += 1
            elif 'Views' in str(tags[tag + i].text):
                value = int(str(tags[tag + i - 1].text).replace('M', ''))*1000000
                views.append(value)
                ticket.append(True)
                print(len(ticket), value)
                i += 1
            else:
                i += 1
info['hashtags'] = hashtags
info['posts'] = posts
info['views'] = views

output_file = 'output.txt'
output_xlsx = 'output.xlsx'

with open(output_file, 'w', encoding='utf-8') as f:
    tags = [str(item) + '\n' for item in tags]
    f.writelines(tags)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
