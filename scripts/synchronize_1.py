import os
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files, analizar_srt


# Aca debe escogerse el directorio audios dentro del directorio "Sin audios"
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

files = find_files(directory, 'traducido.srt')
print(files)

# Creando el archivo de prompts
md_file = os.path.join(directory, 'prompts1.md')

# Añadiendo seccion de prompt1
with open(md_file, "w", encoding="utf-8") as f:
    string = '# prompt1 \n\n'
    f.writelines(string)

md_lines = [string]
for i in range(len(files)):

    print(files[i])

    name_srt = str(files[i]).replace('.srt', '') + ' - modificado.srt'
    output_srt = os.path.join(directory, 'srt', name_srt)
    with open(output_srt, "w", encoding="utf-8") as f:
        f.writelines('')

    with open(files[i], "r", encoding="utf-8") as f:
        r_lines = f.read()
    
    line = \
f'''## {str(os.path.basename(files[i])).replace('.srt', '')}
Te pasaré un archivo de subtitulos srt, con un numero encerrado entre corchetes registrado al final de cada marca temporal correspondiente a cada subtitulo al que llamaremos "x". Reemplaza los subtitulos para que cada subtitulo sea modificado por otra unica linea, solo en caso de que su numero de caracteres sea mayor a su valor "x" correspondiente. En dicho caso la linea rectificada debe ser, sin palabras abreviadas, y su numero de caracteres menor o igual a su valor "x" correspondiente. Deja las marcas temporales:

```srt
{r_lines}
```

'''
   
    md_lines.append(line)

with open(md_file, "w", encoding="utf-8") as f:
    f.writelines(md_lines)
