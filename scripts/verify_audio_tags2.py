import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files


def evaluar_sincronizacion(audio_url, ext1, ext2):
    import os
    from sync_voice_over.sync_voice_over import name_detector, get_mp3_duration

    audio_dir = os.path.dirname(audio_url)
    audio_name = name_detector(audio_url)[0]

    audio1_url = os.path.join(audio_dir, audio_name + ext1)
    audio2_url = os.path.join(audio_dir, audio_name + ext2)
    audio1_duracion = get_mp3_duration(audio1_url)
    audio2_duracion = get_mp3_duration(audio2_url)

    # Imprimir la duración
    try:
        output = [
            audio_name,
            audio1_duracion,
            audio2_duracion,
            abs(audio1_duracion - audio2_duracion),
        ]
    except:
        output = [
            audio_name,
            audio1_duracion,
            audio2_duracion,
            f'{audio1_duracion} - {audio2_duracion}',
        ]
    
    return output


root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

# Definimos la extension de los archivos originales
ext1 = '.mp3'
# Definimos las extensiones de los archivos a sincronizar
ext2 = ' - traducido.mp3'
ext3 = ' - modificado.mp3'
# Medimos sincronizacion
traducidos_output = []
modificados_output = []
files = find_files(directory, ext1)
for audio_url in files:
    if ext2 in audio_url:
        traducidos_output.append(evaluar_sincronizacion(audio_url, ext1, ext2))
    elif ext3 in audio_url:
        modificados_output.append(evaluar_sincronizacion(audio_url, ext1, ext3))

# Creamos los dataframes de reporte
columns = ['name', 'video', 'audio', 'diference']
df1 = pd.DataFrame(traducidos_output, columns=columns)
df2 = pd.DataFrame(modificados_output, columns=columns)

# Mostramos los repotes
print('\nEvaluacion con traducidos')
print(df1)
print('\nEvaluacion con modificados')
print(df2)

# # Exportando salida
# ask = input('Desea exportar resultados? (S/N): ')
# while True:
#     if ask.lower() == 's':
#         output_file = os.path.join(directory, 'report.xlsx')
#         df.to_excel(output_file)
#         break        
#     elif ask.lower() == 'n':
#         break        
#     else:
#         print('Opcion Invalida!')
