Tengo el siguiente segmento de codigo:

```python
response = requests.get(url)
html_content = response.content
```

Pero la "html_content" esta saliendo solo como una linea de apenas 1125 columnas.

Es posible ampliar la informacion que el request es capaz de capturar para que el "html_content" pueda ofrecer mas informacion al final?