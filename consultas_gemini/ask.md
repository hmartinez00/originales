Para extraer el contenido de texto de la etiqueta `yt-attributed-string` proporcionada, puedes utilizar el siguiente código en Python:

```python
from bs4 import BeautifulSoup

# Crea un objeto BeautifulSoup a partir de la cadena HTML
soup = BeautifulSoup(html, "html.parser")

# Encuentra todas las etiquetas `yt-attributed-string`
comments = soup.find_all("yt-attributed-string")

# Extrae el contenido de texto de cada etiqueta
textos = [comment.text for comment in comments]

# Imprime el resultado
print(textos)
```

Esto imprimirá una lista con los tres fragmentos de texto contenidos en las etiquetas `yt-attributed-string` proporcionadas:

```
['Me pregunto¿ porque alguien podria darle "no me gusta" al video de alguien q trata de enseñarte algo?, sobre todo algo tan delicioso, me encanta como explica sus recetas y ademas se ven todas exquisitas, muchas gracias', 'Me quedo tan buena que ahora es el postre que mas vendo. Gracias, Esbieta.', 'Desde que te conocimos, ya no necesitamos ninguna escuela de cocina. Las superaste a todas!! Gracias por tu canal. Es una maravilla!']
```