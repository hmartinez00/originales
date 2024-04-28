import json

def json_query(file: str):
    # Abrir el archivo JSON
    with open(file, 'r') as f:
        data = json.load(f)

    return data

def dir_access(file_key: str) -> str:
    file = r'settings\routes\routes.json'
    json_file = json_query(file)['directories'][file_key]
    
    return json_file
