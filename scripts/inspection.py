import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.module_extractor import extract_values_tag, download_video


urls = [
    'https://pin.it/1rl8tUIn3',
    'https://pin.it/5UAG8iZW4',
    'https://pin.it/61zJzk19Z',
    'https://pin.it/4ysyJqlwe',
    'https://pin.it/6bhGRDJge',
    'https://pin.it/6JStDi4Pu',
    'https://pin.it/2OlX4rqQO',
    'https://pin.it/fUqtnGJcb',
    'https://pin.it/1RuEqesXI',
    'https://pin.it/2d4exY0Nq',
]

top = len(urls)
titles = []
paragraphs = []
for i in range(top):
    url = urls[i]
    title = str(extract_values_tag(url, 'h1')[0]).replace(' ', '_').replace('/', '_')
    titles.append(title)
    paragraph = '\n'.join(extract_values_tag(url, 'span'))
    paragraphs.append(paragraph)
    print(f'{i + 1} de {top}', title)

# Exportar a excel
data = pd.DataFrame({
    'urls'      : urls,
    'titles'    : titles,
    'paragraphs': paragraphs,
})

print(data)

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

file = os.path.join(directory, 'summary.xlsx')
data.to_excel(file, index=False)

