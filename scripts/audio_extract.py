import os
import tkinter as tk
import moviepy.editor
from tkinter import filedialog
from sync_voice_over.sync_voice_over import find_files

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()
ext = '.mp4'

files = find_files(directory, ext)

# Define the directory path
directory_path = os.path.join(directory, "audios")

# Check if the directory exists
if not os.path.exists(directory_path):
    # Create the directory if it doesn't exist
    try:
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

for i in range(len(files)):
    file = files[i]
    filename = str(os.path.basename(file)).replace(ext, '').replace(' ', '_')
    # Se enviará todo al directorio: **audios**
    output = os.path.join(directory_path, filename + '.mp3')
    cvt_video = moviepy.editor.VideoFileClip(file)
    ext_audio = cvt_video.audio
    ext_audio.write_audiofile(output)