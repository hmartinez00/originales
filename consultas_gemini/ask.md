Sí, hay algunas formas de ampliar la información que el request puede capturar para que `html_content` ofrezca más información:

**1. Aumentar el tamaño del búfer de respuesta:**

```python
response = requests.get(url, stream=True)
response.raw.read(500000)  # Aumenta el tamaño del búfer a 500,000 bytes
html_content = response.content
```

**2. Usar la codificación correcta:**

Algunos sitios web pueden tener codificaciones de texto diferentes, como UTF-8 o ISO-8859-1. Intenta utilizar el parámetro `encoding` para especificar la codificación correcta:

```python
response = requests.get(url, encoding='utf-8')
html_content = response.content
```

**3. Deshabilitar la compresión:**

Algunos servidores pueden comprimir las respuestas para ahorrar ancho de banda. Intenta deshabilitar la compresión mediante el parámetro `allow_redirects`:

```python
response = requests.get(url, allow_redirects=False)
html_content = response.content
```

**4. Usar un navegador sin cabeza:**

Una alternativa es utilizar un navegador sin cabeza, como Selenium, para cargar la página web y capturar el HTML completo:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url)
html_content = driver.page_source
```