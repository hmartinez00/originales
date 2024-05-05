import requests
from bs4 import BeautifulSoup


url = "https://www.tiktok.com/tag/pasteleria"
response = requests.get(url, stream=True)
# content_length = int(response.headers['Content-Length'])

# if content_length < 50000:
html_content = response.json()

print(html_content)
# for item in html_content:
#     print(item)


# soup = BeautifulSoup(html_content, 'html.parser')

# output_file = 'output.txt'
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.write(str(soup))

