# Importamos Gemini Pro, textwrap, IPython, sys, para soporte Para Caracteres Especiales en la Terminal de Python 
import tkinter as tk
from tkinter import filedialog
from sync_voice_over.ai_secure_query import process_command


# Seleccionamos el directorio
root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()

ext2 = ' - traducido.srt'
final_ext2 = ' - copy.md'
command2 = 'Voy a publicar un video de esta receta en Facebook e instagram. Crea un copy atractivo con estructura AIDA, de 5 frases de menos de 100 caracteres y un emoticon por cada frase para crear el texto de la publicacion. Agrega al principio un titulo viral con su emoticon. Agrega al final la lista de ingredientes de esta receta y sus cantidades y 9 Hashtags en castellano. No digas nada sobre su preparacion.'
process_command(directory, ext2, final_ext2, command2)
