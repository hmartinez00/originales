import os
import re
import shutil
import mutagen.mp3

def find_files(directory, ext):
    f_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                f_files.append(os.path.join(root, file))
    return f_files

def find_all_files(directory, extensions):
    # Buscando archivos
    files = []
    for ext in extensions:
        # print(ext)
        lista = find_files(directory, ext)
        files.extend(lista)

    return files

def name_detector(file_url):
    directory = os.path.dirname(file_url)
    filename = os.path.basename(file_url)
    if ' - ' in filename:
        tag = filename.split(' - ')[0]
    else:
        tag = filename.split('.')[0]
    
    # Identificar archivos de lote
    archivos_asociados = []
    for archivo in os.listdir(directory):
        if tag in archivo:
            archivos_asociados.append(os.path.join(directory, archivo))

    return tag, archivos_asociados

def move_batch(file_url, directory):
    file_list = name_detector(file_url)[1]
    for file in file_list:
        new_file = os.path.join(directory, os.path.basename(file))
        shutil.move(file, new_file)

def analizar_srt(original_srt, traduccion_srt):
    """
    Función para analizar un archivo de subtítulos SRT.

    Parámetros:
        original_srt (str): Ruta al archivo SRT.

    Salida:
        Imprime en la consola la longitud en caracteres de cada línea de subtítulo.
    """

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


def get_video_duration(srt_file_path):
    """Extrae la duración del vídeo desde un archivo SRT.

    Args:
        srt_file_path (str): Ruta al archivo SRT.

    Devuelve:
        str: Duración del vídeo en formato "hh:mm:ss.sss".
    """

    # Lee el archivo SRT.
    with open(srt_file_path, "r") as f:
        srt_text = f.read()

    # Extrae los sellos de tiempo del archivo SRT.
    timestamps = re.findall(r"(\d+:\d+:\d+,\d+)", srt_text)

    if not timestamps:
        raise ValueError("No se encontraron sellos de tiempo en el archivo SRT.")

    # Calcula la duración del vídeo.
    duration_str = timestamps[-1].split(':')

    # Extraer horas, minutos y segundos
    horas = int(duration_str[0])
    minutos = int(duration_str[1])
    segundos = float(str(duration_str[2]).replace(',', '.'))

    # Convertir el tiempo a segundos
    tiempo_segundos = (horas * 3600) + (minutos * 60) + segundos


    return round(tiempo_segundos)

def get_mp3_duration(audio_url):

    if os.path.isfile(audio_url):
        # Obtener el archivo MP3
        audio = mutagen.mp3.MP3(audio_url)

        # Obtener la duración en segundos
        audio_duracion = round(audio.info.length)
    else:
        audio_duracion = "Error!"
    
    return audio_duracion