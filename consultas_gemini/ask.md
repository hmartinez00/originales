```python
from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>Ejemplo</title>
    </head>
    <body>
        <a href="pagina1.html" title="Página 1">Enlace 1</a>
        <a href="pagina2.html">Enlace 2</a>
        <a href="pagina3.html" title="Página 3">Enlace 3</a>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# Obtener todas las etiquetas 'a'
etiquetas_a = soup.find_all('a')

# Crear una lista para almacenar los títulos
titulos = []

# Iterar sobre las etiquetas 'a' y obtener el título
for etiqueta_a in etiquetas_a:
    titulo = etiqueta_a.get('title')
    if titulo:
        titulos.append(titulo)

print(titulos)
```

**Salida:**

```
['Página 1', 'Página 3']
```