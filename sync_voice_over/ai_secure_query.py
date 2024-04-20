import os
import subprocess
from sync_voice_over.sync_voice_over import find_files


def ai_secure_query(command):
    # Obtenemos la respuesta 
    file_script = "scripts/app.py"
    input_file = r'consultas_gemini\quest.md'
    output_file = r'consultas_gemini\ask.md'

    # Limpiamos el archivo de respuesta ask
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines('')    

    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(command)
    subprocess.run(["python", file_script])

    while True:
        eleccion = input("¿Desea conservar las respuesta (S/N)? ")
        if eleccion.lower() == "n":
            subprocess.run(["python", file_script])

        elif eleccion.lower() == "s":
            break
        else:
            print("Opción no válida. Ingrese 'S' para continuar o 'N' para detenerse.")

    with open(output_file, 'r', encoding='utf-8') as archivo:
        # Leer el contenido del archivo
        r_linea = archivo.read()
    ask = r_linea

    return ask

def process_command(directory, ext, final_ext, command):

    files = find_files(directory, ext)
    for file in files:
        # Abrir el archivo en modo lectura
        print(file)
        with open(file, 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            r_linea = archivo.read()

        dirname = os.path.dirname(file)
        filename = str(os.path.basename(file)).replace(ext, '') + final_ext
        output_file = os.path.join(dirname, filename)
        
        prompt = \
f'''{command}

{r_linea}'''

        print(output_file)
        print(prompt)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines('')
        ask = ai_secure_query(prompt)
        print(ask)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(ask)
