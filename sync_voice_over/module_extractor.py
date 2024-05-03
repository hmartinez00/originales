import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def extract_values_tag(url: str, tag: str) -> list:

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract values content after interacting with elements
    values = soup.find_all(tag)
    content = []
    for value in values:
        # content.append(value.text)
        content.append(value)
    
    return content

def html_format(file):

    # Leer el código HTML desde un archivo
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()

    # Reemplazar múltiples espacios en blanco con un solo espacio
    html = re.sub(" +", " ", html)

    # Agregar saltos de línea después de las etiquetas de apertura y cierre
    html = html.replace(">", ">\n")
    html = html.replace("<", "\n<")

    # Agregar sangría a las etiquetas anidadas
    indentacion = 0
    lineas = html.split("\n")
    for i, linea in enumerate(lineas):
        if linea.startswith("</"):
            indentacion -= 1
        lineas[i] = " " * indentacion + linea
        if linea.startswith("<"):
            indentacion += 1

    # Unir las líneas y escribir el código HTML corregido en un archivo
    output_lines = "\n".join(lineas)

    return output_lines


def download_video(url, link, title, directory):

    driver = webdriver.Chrome()
    x_path_link = '//*[@id="download_input"]'
    x_path_button = '//*[@id="download_button"]'
    x_path_download = '//*[@id="video_down"]'
    x_path_video = '/html/body/video/source'
    driver.get(url)

    driver.find_element(By.XPATH, x_path_link).send_keys(link)
    driver.find_element(By.XPATH, x_path_button).click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, x_path_download).click()

    right_click = driver.find_element(By.XPATH, x_path_video)
    video_url = right_click.get_attribute('src')
    print(title)

    response = requests.get(video_url)
    if response.status_code == 200:
        video_data = response.content
        title = os.path.join(directory, title + '.mp4')
        with open(title, 'wb') as f:
            f.write(video_data)
        print("Video descargado correctamente")
    else:
        print("Error al descargar el video:", response.status_code)
    driver.implicitly_wait(10)

def download_video_tiktok(url, link, title, directory):

    driver = webdriver.Chrome()
    x_path_link = '//*[@id="s_input"]'
    x_path_button = '//*[@id="search-form"]/button'
    x_path_download = '//*[@id="search-result"]/div[2]/div/div[2]/div/p[3]/a'
    driver.get(url)

    driver.find_element(By.XPATH, x_path_link).send_keys(link)
    time.sleep(2)
    driver.find_element(By.XPATH, x_path_button).click()
    driver.implicitly_wait(10)

    right_click = driver.find_element(By.XPATH, x_path_download)
    video_url = right_click.get_attribute('href')
    print(video_url)

    response = requests.get(video_url)
    if response.status_code == 200:
        video_data = response.content
        title = os.path.join(directory, title + '.mp4')
        with open(title, 'wb') as f:
            f.write(video_data)
        print("Video descargado correctamente")
    else:
        print("Error al descargar el video:", response.status_code)
    driver.implicitly_wait(10)

def web_query(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    input('Press to continue: ')
    driver.close()


