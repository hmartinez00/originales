import os
import json


ruta_archivo_json = r'settings\routes\routes.json'

script_name = input('Introduzca el nombre del nuevo script: ').lower().replace(' ', '_')
new_menu    = input('Introduzca el nombre del nuevo menu: ').capitalize()
new_script  = os.path.join('scripts', script_name + '.py')

with open(new_script, 'w') as file:
    file.write('')

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

datos_json['exec'][0].append(new_menu)
datos_json['exec'][1].append(new_script)

with open(ruta_archivo_json, 'w') as f:
    json.dump(datos_json, f, indent=4)