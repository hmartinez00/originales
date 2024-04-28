import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.json_queries import dir_access, json_query, date_str, export
from sync_voice_over.module_extractor import extract_values_tag, download_video

date = date_str()

# Replace with the desired URL
url = "https://pinterestdownloader.com/es"
key='urls'
json_file = dir_access(key)
links = json_query(json_file)[key]

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

top = len(links)
titles = []
paragraphs = []
for i in range(top):
    link = links[i]
    title = str(extract_values_tag(link, 'h1')[0]).replace(' ', '_').replace('/', '_')
    titles.append(title)
    paragraph = '\n'.join(extract_values_tag(link, 'span'))
    paragraphs.append(paragraph)
    print(f'{i + 1} de {top}', title)
    download_video(url, link, title, directory)

# Exportar a csv
data = pd.DataFrame({
    'links'     : links,
    'titles'    : titles,
    'paragraphs': paragraphs,
})
file = os.path.join(directory, 'summary_' + date + '.xlsx')
export(data, file)
