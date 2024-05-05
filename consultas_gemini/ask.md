**Opción 1: Usando el método `set()`**

El tipo de datos `set` en Python no permite duplicados. Puedes convertir tu lista en un conjunto y luego convertirlo de nuevo a una lista para eliminar los duplicados:

```python
lista = [1, 2, 3, 4, 1, 2, 5]
lista_sin_duplicados = list(set(lista))
```

**Opción 2: Usando un bucle y el método `index()`**

Puedes iterar sobre la lista y para cada elemento, usar el método `index()` para encontrar su primer índice de aparición. Si el índice del elemento es diferente del índice actual, significa que es un duplicado y se puede eliminar:

```python
lista = [1, 2, 3, 4, 1, 2, 5]

i = 0
while i < len(lista):
    if lista[i] in lista[i+1:]:
        lista.pop(i)
    else:
        i += 1
```

**Opción 3: Usando un diccionario**

Puedes crear un diccionario donde las claves sean los elementos de la lista. Como los diccionarios no permiten claves duplicadas, esto eliminará automáticamente los duplicados:

```python
lista = [1, 2, 3, 4, 1, 2, 5]

elementos_unicos = {}
for elemento in lista:
    elementos_unicos[elemento] = True

lista_sin_duplicados = list(elementos_unicos.keys())
```