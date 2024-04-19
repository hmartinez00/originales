import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files


def evaluar_sincronizacion(audio_url):
    import os
    import mutagen.mp3
    from sync_voice_over.sync_voice_over import get_video_duration

    # Extrayendo los nombres del archivo y el directorio local
    audio_dir = os.path.dirname(audio_url)
    audio_name = os.path.basename(audio_url)

    # Obtener el archivo MP3
    audio = mutagen.mp3.MP3(audio_url)

    # Obtener la duración en segundos
    audio_duracion = round(audio.info.length)

    # Ejemplo de uso
    srt_file_name = audio_name.replace('.mp3', '.srt')
    srt_file_path = os.path.join(audio_dir, srt_file_name)
    video_duration = get_video_duration(srt_file_path)

    # Imprimir la duración

    output = [
        audio_name,
        audio_duracion,
        video_duration,
        abs(audio_duracion - video_duration),
    ]
    
    return output


root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()
ext = '.mp3'

general_output = []
files = find_files(directory, ext)
for audio_url in files:
    general_output.append(evaluar_sincronizacion(audio_url))

columns = ['name', 'audio', 'video', 'diference']

# Convertir la lista en un dataframe
df = pd.DataFrame(general_output, columns=columns)

# Mostrar el dataframe
print(df)
output_file = os.path.join(directory, 'report.xlsx')
df.to_excel(output_file)