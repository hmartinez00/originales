import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_values_tag(url, tag):

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract values content after interacting with elements
    values = soup.find_all(tag)
    content = []
    for value in values:
        content.append(value.text)
    
    return content

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

