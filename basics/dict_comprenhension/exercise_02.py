"""
Ejercicio 2: Filtrar Personas Mayores de Edad
Enunciado:
Dado el diccionario edades = {"Ana": 17, "Luis": 22, "Carlos": 15, "María": 20}, crea un nuevo diccionario que solo contenga a las personas con edad mayor o igual a 18 años.
Solución Esperada:
{"Luis": 22, "María": 20}
"""
edades = {"Ana": 17, "Luis": 22, "Carlos": 15, "María": 20}
edades = {nombre: edad for nombre, edad in sorted(edades.items(), key=lambda x: x[0], reverse=True)}
mayores = {nombre: edad for nombre, edad in edades.items() if edad >= 18}
print(mayores)