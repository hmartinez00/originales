El código falla porque está intentando escribir una lista de objetos BeautifulSoup en un archivo de texto. Para escribirlas correctamente, deberías convertir cada objeto BeautifulSoup a una cadena antes de escribirlo en el archivo.

Aquí tienes el código corregido:

```python
output_file = 'output.txt'

soup = BeautifulSoup(html_tags, "lxml")
values = soup.find_all('a')

with open(output_file, 'w', encoding='utf-8') as f:
    for value in values:
        f.write(str(value) + '\n')
```