Puedes usar la función `re.sub` con la expresión regular apropiada para reemplazar los saltos de línea por el carácter de nueva línea (`\n`):

```python
import re

html = "<html><body><h1>Un ejemplo de HTML en una <span>sola línea</span></h1></body></html>"

html = re.sub(r'(?=<[^>]*>)', '\n', html)

print(html)
```

Salida:

```html
<html>
<body>
<h1>Un ejemplo de HTML en una <span>sola línea</span></h1>
</body>
</html>
```