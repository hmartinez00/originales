# Importamos Gemini Pro, textwrap, IPython, sys, para soporte Para Caracteres Especiales en la Terminal de Python 
import google.generativeai as genai 
import textwrap 
from IPython.display import Markdown 
import sys
import json
import os
import tkinter as tk
from tkinter import filedialog
# from General_Utilities.sync_voice_over import find_All_files


sys.stdout.reconfigure(encoding='utf-8')

# Usamos el modelo generativo de la IA 
modelo = genai.GenerativeModel('gemini-pro')

# Abrir el archivo JSON
with open(r'settings\api\settings.json', 'r') as f:
    data = json.load(f)

# Configuramos la API KEY 
GOOGLE_API_KEY=data['api']
genai.configure(api_key=GOOGLE_API_KEY)

def process_command(model, _directory, ext, final_ext, command):
    import os
    import subprocess

    # Rebajamos el tamaño de la respuesta de la IA 
    def rebajar(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def ai_query(model, command):
        # Obtenemos la respuesta 
        ask = model.generate_content(command)
        ask = ask.text
        # ask = ask.candidates[0].content.parts
        # print(ask)
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     f.writelines(ask)

        return ask

    def ai_secure_query(command):
        # Obtenemos la respuesta 
        input_file = r'consultas_gemini\quest.md'
        output_file = r'consultas_gemini\ask.md'

        with open(input_file, 'w', encoding='utf-8') as f:
            f.writelines(command)
        subprocess.run(["python", "scripts/app.py"])

        while True:
            eleccion = input("¿Desea conservar las respuesta (S/N)? ")
            if eleccion.lower() == "n":
                subprocess.run(["python", "scripts/app.py"])

            elif eleccion.lower() == "s":
                break
            else:
                print("Opción no válida. Ingrese 'S' para continuar o 'N' para detenerse.")

        with open(output_file, 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            r_linea = archivo.read()
        ask = r_linea

        return ask

    def find_All_files(_directory, ext):
        f_files = []
        for root, _, files in os.walk(_directory):
            for file in files:
                if file.endswith(ext):
                    f_files.append(os.path.join(root, file))
        return f_files

    files = find_All_files(_directory, ext)
    for file in files:
        print(file)
        # Abrir el archivo en modo lectura
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
        # try:
        #     ask = ai_query(model, prompt)
        # except OSError as e:
        #     ask = f"Error creating file: {e}"
        ask = ai_secure_query(prompt)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(ask)
        


# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()


ext1 = '.srt'
final_ext1 = ' - traducido.srt'
command1 = 'Traduce el siguiente archivo de subtitulos al castellano. Entrega el resultado en formato de archivo srt con las misma marcas de tiempo que ya tiene.'
process_command(modelo, directory, ext1, final_ext1, command1)

ext2 = 'traducido.srt'
final_ext2 = ' - copy.md'
command2 = 'Voy a publicar un video de esta receta en Facebook e instagram. Crea un copy atractivo con estructura AIDA, de 5 frases de menos de 100 caracteres para crear el texto de la publicacion. Agrega al final la lista de ingredientes de esta receta y sus cantidades y 9 Hashtags en castellano. No digas nada sobre su preparacion.'
process_command(modelo, directory, ext2, final_ext2, command2)

