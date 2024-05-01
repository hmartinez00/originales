import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_elements(keyword, num_results):

    base_url = "https://www.tiktok.com/discover/{}?lang=es"
    url = base_url.format(keyword)
    response = requests.get(url)
    results = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h4_topic_elements = soup.find_all("h4", attrs={"data-e2e": "topic-name"})
        h4_hashtags_elements = soup.find_all("h4", attrs={"data-e2e": "hashtags-name"})

        keywords = [h4.text.strip() for h4 in h4_topic_elements[:num_results]]
        hashtags = [h4.text.strip() for h4 in h4_hashtags_elements[:num_results]]

        for kw in keywords:
            results.append((keyword, kw, hashtags))

    return results

def format_keyword(keyword: str) -> str:
    return keyword.replace(" ", "-")

initial_keyword = input("Por favor, introduce la palabra clave inicial: ")
formatted_keyword = format_keyword(initial_keyword)

base_url = "https://www.tiktok.com/discover/{}?lang=es"
url = base_url.format(formatted_keyword)
response = requests.get(url)

if response.status_code == 200:
    iterations = int(input("Por favor, introduce el numero de veces que quieres ejecutar el bucle: "))
    num_results = int(input("Por favor, introduce el numero de resultados que deseas obtener en cada iteracion: "))
    
    initial_keywords = [formatted_keyword]
    all_results = []

    for _ in range(iterations):
        new_results = []
        for keyword in initial_keywords:
            elements = get_elements(keyword, num_results)
            new_results.extend(elements)
        initial_keywords = [format_keyword(result[1]) for result in new_results]
        all_results.extend(new_results)

    print(all_results)

    columns = ["Initial Keyword", "Keyword", "Hashtags"]
    # data = [[result[0], result[1], ", ".join(result[2])] for result in all_results]

    # df = pd.DataFrame(data, columns=columns)
    # print(df)
else:
    print("La palabra clave no devolvió una respuesta válida. Por favor, intenta con otra palabra clave.")
