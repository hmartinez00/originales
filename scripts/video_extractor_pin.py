import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.json_queries import dir_access, json_query
from sync_voice_over.module_extractor import extract_values_tag, download_video


# Replace with the desired URL
url = "https://pinterestdownloader.com/es"
key='urls'
json_file = dir_access(key)
links = json_query(json_file)[key]

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

# Define the directory path
directory_path = os.path.join(directory, "videos")

# Check if the directory exists
if not os.path.exists(directory_path):
    # Create the directory if it doesn't exist
    try:
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

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
    download_video(url, link, title, directory_path)


# Exportar a csv
data = pd.DataFrame({
    'links'     : links,
    'titles'    : titles,
    'paragraphs': paragraphs,
})
file = os.path.join(directory_path, 'summary.xlsx')
data.to_excel(file)
