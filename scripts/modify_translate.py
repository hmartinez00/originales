import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

def analizar_srt(original_srt, traduccion_srt):
    """
    Función para analizar un archivo de subtítulos SRT.

    Parámetros:
        original_srt (str): Ruta al archivo SRT.

    Salida:
        Imprime en la consola la longitud en caracteres de cada línea de subtítulo.
    """

    original_srt = os.path.join(directory, 'audio.srt')
    traduccion_srt = os.path.join(directory, 'audio - traduccion.srt')

    # Expresión regular para las marcas de tiempo
    regex_marca_tiempo = r"^\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+$"

    with open(original_srt, "r") as f:
        lineas = f.readlines()

    with open(traduccion_srt, "r") as f:
        t_lineas = f.readlines()
    
    mark_index = [False for _ in range(len(lineas))]

    # Bucle para iterar por las líneas
    for i, linea in enumerate(lineas):
        # Si la línea actual es una marca de tiempo
        if re.match(regex_marca_tiempo, linea):
            # Obtener la siguiente línea (asumiendo que es el subtítulo)
            subtitulo = lineas[i + 1]
            # Eliminar saltos de línea
            subtitulo = subtitulo.strip()
            # calcular el numero de caracteres
            longitud = len(subtitulo) + 1
            # Tomando el indice de marca temporal
            mark_index[i] = lineas[i].replace('\n', '') + f" [{longitud}]" + '\n'
            # Modificar la línea de marca de tiempo
            lineas[i] = mark_index[i]

    # Bucle para iterar por las líneas
    for i, t_linea in enumerate(t_lineas):
        # Si la línea actual es una marca de tiempo
        if re.match(regex_marca_tiempo, t_linea):
            # Modificar la línea de marca de tiempo
            t_lineas[i] = mark_index[i]

    # Escribir las líneas modificadas al archivo
    with open(original_srt, "w") as f:
        f.writelines(lineas)

    # Escribir las líneas modificadas al archivo
    with open(traduccion_srt, "w") as f:
        f.writelines(t_lineas)


# Ejemplo de uso
original_srt = "audio copy.srt"
traduccion_srt = "audio - traduccion copy.srt"
analizar_srt(original_srt, traduccion_srt)
