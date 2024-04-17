from datetime import datetime as dt


fecha = dt.now()
filename = f'{fecha.date()}_{fecha.hour}{fecha.minute}{fecha.second}'

print(filename)
input_quest_file = f'consultas_gemini/quest.md'
input_ask_file = f'consultas_gemini/ask.md'
output_file = f'consultas_gemini/backups/{filename}.md'

with open(input_quest_file, 'r', encoding='utf-8') as f:
    quest_contenido = f.read()
with open(input_ask_file, 'r', encoding='utf-8') as f:
    ask_contenido = f.read()

contenido = \
f'''# Prompt:
{quest_contenido}

========================
# Ask:
{ask_contenido}
'''

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(contenido)