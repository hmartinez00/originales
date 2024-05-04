Para obtener todas las coincidencias de una subcadena dentro de una cadena más grande en Python, puedes utilizar el método `findall()`. Este método devuelve una lista de todas las coincidencias de la subcadena en la cadena, manteniendo el orden en que aparecen.

**Sintaxis:**

```
cadena.findall(subcadena)
```

**Ejemplo:**

```python
cadena = "Hola mundo, hola Python"
subcadena = "hola"

coincidencias = cadena.findall(subcadena)
print(coincidencias)
```

**Salida:**

```
['hola', 'hola']
```

El método `findall()` también acepta expresiones regulares como argumento. Esto te permite realizar coincidencias más complejas. Por ejemplo, para obtener todas las coincidencias de palabras que comiencen con "h" en la cadena, podrías usar la siguiente expresión regular:

```python
import re

cadena = "Hola mundo, hola Python"
subcadena = re.compile(r'\bh\w+')

coincidencias = cadena.findall(subcadena)
print(coincidencias)
```

**Salida:**

```
['Hola', 'hola']
```