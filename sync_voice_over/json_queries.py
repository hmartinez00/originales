import json
import pandas as pd
from datetime import datetime as dt

def date_str():
    date = '_'.join(str(i) for i in tuple(dt.now().timetuple())[:6])
    
    return date

def json_query(file: str):
    # Abrir el archivo JSON
    with open(file, 'r') as f:
        data = json.load(f)

    return data

def dir_access(file_key: str) -> str:
    file = r'settings\routes\routes.json'
    json_file = json_query(file)['directories'][file_key]
    
    return json_file

def export(df: pd.DataFrame, output_file: str):
    # Exportando salida
    ask = input('Desea exportar resultados? (S/N): ')
    while True:
        if ask.lower() == 's':
            df.to_excel(output_file)
            break        
        elif ask.lower() == 'n':
            break        
        else:
            print('Opcion Invalida!')
