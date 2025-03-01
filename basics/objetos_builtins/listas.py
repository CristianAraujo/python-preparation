# Date: March 01, 2025

from pprint import pprint as pp

"""
1. List (Lista)
Descripción: Una lista es una colección ordenada y mutable de elementos. 
Permite almacenar múltiples elementos de diferentes tipos (números, cadenas, objetos, etc.) 
en una sola estructura.

Características:
Ordenada: Mantiene el orden de los elementos.
Mutable: Puedes agregar, eliminar y modificar elementos.
Indexada: Los elementos se acceden por índice, comenzando desde 0.

Métodos comunes:
1. append(x): Agrega un elemento al final de la lista.
2. extend(iterable): Extiende la lista añadiendo los elementos de otra lista.
3. insert(i, x): Inserta el elemento x en la posición i de la lista.
4. pop(): Elimina y devuelve el último elemento (o un índice específico).
5. sort(): Ordena los elementos de la lista.
"""
# 1. append(x): Agrega un elemento al final de la lista.
grupo1 = [22, 24, 32, 41, 50]
grupo1.append(90)
print(f'grupo1.append(90): {grupo1}')

# 2. extend(iterable): Extiende la lista añadiendo los elementos de otra lista.
grupo2 = [11, 9, 12, 17]
grupo1.extend(grupo2)
print(f'grupo1.extend(grupo2): {grupo1}')

# 3. insert(i, x): Inserta el elemento x en la posición i de la lista.
letras = ['a', 'c', 'd']
letras.insert(1, 'b')
print(f'letras.insert(1, b): {letras}')

# 4. remove(): Elimina la primera aparición del elemento x de la lista..
nombres = ['cristian', 'carlos', 'claudia', 'eduardo', 'jessica']
nombres.remove('carlos')
print(f'nombres.remove(0): {nombres}')


# 5. pop([i]): Elimina y devuelve el elemento en la posición i. Si no 
# se especifica i, elimina y devuelve el último elemento de la lista.
paises = ['chile', 'filipinas', 'holanda', 'tailandia', 'peru', 'polonia']
print(f'paises: {paises}')
pais_removido = paises.pop()
print(f'pais_removido: {pais_removido}')
print(f'paises.pop(): {paises}')
pais_removido = paises.pop(1)
print(f'pais_removido: {pais_removido}')
print(f'paises.pop(1): {paises}')


# 6. clear(): Elimina todos los elementos de la lista, dejándola vacía.
ciudades = ['santiago', 'manila', 'jakarta', 'bagkok', 'lima']
print(f'ciudades: {ciudades}')
ciudades.clear()
print(f'ciudades.clear(): {ciudades}')

# 7. index(x[, start[, end]])
# Devuelve el índice de la primera aparición del elemento x en la lista, 
# opcionalmente buscando en el rango entre los índices start y end.
meses = ['enero', 'marzo', 'enero', 'febrero', 'diciembre']
mes = meses.index('enero')
print(f'mes: {mes}')
mes = meses.index('febrero')
print(f'mes: {mes}')
mes = meses.index('enero', 1, 4)
print(f'mes: {mes}')
mes = meses.index('diciembre', 1, 5)
print(f'mes: {mes}')
# mes = meses.index('diciembre', 1, 5) in 
# print(f'mes: {mes}')

# 8. count(x)
# Descripción: Devuelve el número de veces que el elemento x aparece en la lista.
elementos = [1 ,2, 3, 3, 4, 3, 2]
print(f'apariciones 3: {elementos.count(3)}')
print(f'apariciones 3: {elementos.count(2)}')

# 9. sort(key=None, reverse=False)
# Descripción: Ordena los elementos de la lista in-place (modificando la lista original). 
# Se puede especificar un key para ordenar de acuerdo con una función y un reverse para 
# ordenar en orden descendente.
apellidos = ['araujo', 'bravo', 'oyarzun', 'benitez', 'huanca']
apellidos.sort(key=lambda x: len(x))
print(f'apellidos.sort(key=lambda x: lenf(x)): {apellidos}')
apellidos.sort(key=len, reverse=True)
print(f'apellidos.sort(key=len, reverse=True): {apellidos}')
apellidos.sort(key= lambda x: x[1])
print(f'apellidos.sort(key= lambda x: x[1]): {apellidos}')

def ordenar(elem):
    final_letter = elem[-2]
    return final_letter

apellidos.sort(key=ordenar)
print(f'apellidos.sort(key=ordenar): {apellidos}')

# 10. reverse()
# Descripción: Invierte los elementos de la lista in-place.
notas1 = [1, 4, 5, 3]
print(f'notas1: {notas1}')
notas1.reverse()
print(f'notas1.reverse(): {notas1}')

# 11. copy()
# Descripción: Retorna una copia superficial de la lista.
saludos1 = ['hi', 'hello', 'hola', 'wena']
saludos2 = saludos1.copy()
print(f'saludos1 is saludos2: {saludos1 is saludos2}')
print(f'id(saludos1) | id(saludos2): {id(saludos1)} | {id(saludos2)}')

# 12. del
# Descripción: Permite eliminar elementos de una lista usando un índice o un rango de índices.
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
print(f'dias: {dias}')
del dias[1]
print(f'dias: {dias}')
del dias[0:2]
print(f'dias: {dias}')

# 13. min()
# Descripción: Devuelve el valor mínimo de la lista.
cantidades = [100, 131, 121, 98, 136]
print(f'min(cantidades): {min(cantidades)}')
animales = ['pollo', 'gato', 'cerdo']
print(f'min(animales): {min(animales)}')

# 14. max()
# Descripción: Devuelve el valor máximo de la lista.
cantidades = [100, 131, 121, 98, 136]
print(f'max(cantidades): {max(cantidades)}')
animales = ['pollo', 'gato', 'cerdo']
print(f'max(animales): {max(animales)}')

# 15. sum()
# Descripción: Retorna la suma de todos los elementos de la lista 
# (solo si los elementos son numéricos).
cantidades = [100, 131, 121, 98, 136]
print(f'sum(cantidades): {sum(cantidades)}')
# print(f'sum(animales): {sum(animales)}') # No soportado