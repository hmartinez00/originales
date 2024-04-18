```python
# Crear las 20 listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
# ... y así sucesivamente hasta lista20

# Crear una lista vacía para almacenar la lista concatenada
lista_concatenada = []

# Recorrer las 20 listas y agregar cada elemento a la lista concatenada
for lista in [lista1, lista2, lista3,  # Agregar las 20 listas aquí]:
    lista_concatenada.extend(lista)

# Imprimir la lista concatenada
print(lista_concatenada)
```