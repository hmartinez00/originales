Por que falla este codigo?


output_file = 'output.txt'

soup = BeautifulSoup(html_tags, "lxml")
values = soup.find_all('a')

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(values)