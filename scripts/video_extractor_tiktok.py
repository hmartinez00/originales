import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.module_extractor import extract_values_tag, download_video, download_video_tiktok


url = "https://savetik.co/en"

data = {
    # 'https://vm.tiktok.com/ZMMXaYT2C/': 'recetas de trufas de chocolate',
    # 'https://vm.tiktok.com/ZMMXa4nVG/': 'tecnica de temperado del chocolate',
    # 'https://vm.tiktok.com/ZMMXa3Kto/': 'ciencia del chocolate brillante',
    'https://vm.tiktok.com/ZMMXav1pJ/': 'bombon de chocolate casero',
    'https://vm.tiktok.com/ZMMXmL5rW/': 'arte de la escultura de chocolate',
    'https://vm.tiktok.com/ZMMXmj54G/': 'beneficios del cacao para la salud',
    'https://vm.tiktok.com/ZMMXmVQ8j/': 'recetas saludables con chocolate',
    'https://vm.tiktok.com/ZMMXmCRmG/': 'alternativas al azucar en las',
    'https://vm.tiktok.com/ZMMXmuSnD/': 'recetas de chocolate',
    'https://vm.tiktok.com/ZMMXmCe26/': 'chocolate personalizado para eventos',
    'https://vm.tiktok.com/ZMMXms1w5/': 'regalos de chocolate para San Valentin',
    'https://vm.tiktok.com/ZMMXuMuK6/': 'chocolate tematico para fiestas',
    'https://vm.tiktok.com/ZMMXmw4ha/': 'cursos de fabricacion de chocolate en linea',
}

titles  = list(data.values())
links   = list(data.keys())

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
# titles = []
# paragraphs = []
for i in range(top):
    link = links[i]
    title = titles[i]
    # title = str(extract_values_tag(link, 'h1')[0]).replace(' ', '_').replace('/', '_')
    # titles.append(title)
    # paragraph = '\n'.join(extract_values_tag(link, 'span'))
    # paragraphs.append(paragraph)
    print(f'{i + 1} de {top}', title)
    download_video_tiktok(url, link, title, directory_path)


# # Exportar a csv
# data = pd.DataFrame({
#     'links'     : links,
#     'titles'    : titles,
#     'paragraphs': paragraphs,
# })
# file = os.path.join(directory_path, 'summary.xlsx')
# data.to_excel(file)
