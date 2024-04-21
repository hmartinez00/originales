import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files


def evaluar_sincronizacion(audio_url, ext1, ext2):
    import os
    from sync_voice_over.sync_voice_over import get_video_duration, get_mp3_duration

    # Extrayendo los nombres del archivo y el directorio local
    audio_dir = os.path.dirname(audio_url)
    audio_name = os.path.basename(audio_url)

    audio_duracion = get_mp3_duration(audio_url)

    # Ejemplo de uso
    srt_file_name = audio_name.replace(ext1, ext2)
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
ext1 = '.mp3'
ext2 = ' - traducido.srt'
general_output = []
files = find_files(directory, ext1)
for audio_url in files:
    general_output.append(evaluar_sincronizacion(audio_url, ext1, ext2))

columns = ['name', 'audio', 'video', 'diference']

# Convertir la lista en un dataframe
df = pd.DataFrame(general_output, columns=columns)

# Mostrar el dataframe
print(df)

# Exportando salida
ask = input('Desea exportar resultados? (S/N): ')
while True:
    if ask.lower() == 's':
        output_file = os.path.join(directory, 'report.xlsx')
        df.to_excel(output_file)
        break        
    elif ask.lower() == 'n':
        break        
    else:
        print('Opcion Invalida!')