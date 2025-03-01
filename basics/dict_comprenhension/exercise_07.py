# Date: March 01, 2025

"""
Ejercicio 4: Transformar y ordenar una lista de productos

Enunciado:
Dada la lista de tuplas:

productos = [("manzana", 100), ("banana", 80), ("cereza", 150)]
Crea un diccionario donde:

La clave sea el nombre del producto en mayúsculas.
El valor sea el precio incrementado en un 10%.
Los productos estén ordenados alfabéticamente por su nombre original.
"""
productos = [("manzana", 100), ("banana", 80), ("cereza", 150)]
productos = {nombre.upper(): f'{valor * 1.10:.2f}'
             for nombre, valor 
             in sorted(productos)}
print(productos)
