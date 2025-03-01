# Dict comprenhension
import pprint as pp

"""
Ejercicio 1: Cuadrados de Números
Enunciado:
Dada la lista de números numeros = [1, 2, 3, 4, 5], crea un diccionario donde cada clave sea el número y el valor sea su cuadrado.
Solución Esperada:
"""
numeros = range(1,10)
squares =  {x: x**2 for x in numeros}
pp.pprint(squares)