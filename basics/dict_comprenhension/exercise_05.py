"""
Ejercicio 5: Ordenar por valor (puntaje) en orden ascendente
Enunciado:
Usando el mismo diccionario de estudiantes, crea un nuevo diccionario 
ordenado según los puntajes (valores) de forma ascendente.
"""
camareros = { "Ana": 85, "Luis": 92, "Carlos": 78, "María": 90 }
# pp.pprint(sorted(estudiantes.items(), key=lambda x: x[1]))
camareros = { nombre: puntaje for nombre, puntaje in sorted(camareros.items(), key=lambda x: x[1])}
pp.pprint(f'camareros: {camareros}')