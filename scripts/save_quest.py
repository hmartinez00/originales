from datetime import datetime as dt


fecha = dt.now()
filename = f'{fecha.date()}_{fecha.hour}{fecha.minute}{fecha.second}'

print(filename)
input_file = f'consultas_gemini/ask.md'
output_file = f'consultas_gemini/backups/{filename}.md'

with open(input_file, 'r', encoding='utf-8') as f:
    contenido = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(contenido)