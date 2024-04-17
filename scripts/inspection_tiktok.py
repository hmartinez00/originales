import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.module_extractor import extract_values_tag, download_video


urls = [
    'https://www.tiktok.com/@chocolatseve/video/7354020684303011105?is_from_webapp=1&sender_device=pc',
    # 'https://pin.it/6vCefPwPX',
]

top = len(urls)
titles = []
paragraphs = []
for i in range(top):
    url = urls[i]
    # title = str(extract_values_tag(url, 'h1')[0]).replace(' ', '_').replace('/', '_')
    # titles.append(title)
    paragraph = '\n'.join(extract_values_tag(url, 'a'))
    paragraphs.append(paragraph)
    print(f'{i + 1} de {top}', paragraph)

# # Exportar a excel
# data = pd.DataFrame({
#     'urls'      : urls,
#     'titles'    : titles,
#     'paragraphs': paragraphs,
# })

# print(data)

# root = tk.Tk()
# root.withdraw()
# directory = filedialog.askdirectory()

# file = os.path.join(directory, 'summary.xlsx')
# data.to_excel(file, index=False)

