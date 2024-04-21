Para determinar si una ruta es un archivo existente en Python, puedes utilizar la función `os.path.isfile()`.

**Ejemplo:**

```python
import os.path

ruta = "/ruta/a/mi/archivo.txt"

if os.path.isfile(ruta):
    print("El archivo existe")
else:
    print("El archivo no existe")
```