import requests
import pandas as pd
from bs4 import BeautifulSoup
from sync_voice_over.json_queries import export

url = 'https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en'
id = "CardPc_titleText__RYOWo"

response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
tags = soup.find_all('span')

info = {}
hashtags, posts, views = [], [], []
for tag in range(len(tags)):
    if id in str(tags[tag]):
        hashtags.append(str(tags[tag + 0].text) + '\n')
        print(str(tags[tag + 0].text))
        ticket = []
        i = 1
        while len(ticket) < 2:
            if 'Posts' in str(tags[tag + i].text):
                value = str(tags[tag + i - 1].text)
                posts.append(value + '\n')
                ticket.append(True)
                print(len(ticket), value)
                i += 1
            elif 'Views' in str(tags[tag + i].text):
                value = str(tags[tag + i - 1].text)
                views.append(value + '\n')
                ticket.append(True)
                print(len(ticket), value)
                i += 1
            else:
                i += 1
info['hashtags'] = hashtags
info['posts'] = posts
info['views'] = views

output_file = 'output.txt'
output_xlsx = 'output.xlsx'

with open(output_file, 'w', encoding='utf-8') as f:
    tags = [str(item) + '\n' for item in tags]
    f.writelines(tags)

df = pd.DataFrame.from_dict(info)
print(df)
export(df, output_xlsx)
