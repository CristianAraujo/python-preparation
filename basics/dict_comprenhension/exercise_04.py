
"""
Ejercicio 4: Ordenar por clave (nombre) en orden descendente

Enunciado:
Dado el diccionario:

estudiantes = {"Ana": 85, "Luis": 92, "Carlos": 78, "María": 90}

Crea un nuevo diccionario en el que los estudiantes se encuentren 
ordenados por su nombre en orden descendente.
"""
estudiantes = { "Ana": 85, "Luis": 92, "Carlos": 78, "María": 90 }
estudiantes = {nombre: edad for nombre, edad in sorted(estudiantes.items(), key=lambda x:x[0])}
print(estudiantes)

estudiantes = { "Amalia": 85, "Gustavo": 92, "Miguel": 78, "Zazo": 90 }
estudiantes = { nombre: estudiantes[nombre] for nombre in sorted(estudiantes, reverse=True)}
print(estudiantes)