# Date: March 01, 2025


"""
Ejercicio 3: Filtrar y ordenar un diccionario de palabras

Enunciado:
Dado el diccionario:

palabras = {"a": 5, "hola": 10, "python": 7, "programacion": 4, "es": 3}

Crea un nuevo diccionario que incluya únicamente las palabras con más de 3 
caracteres, y que esté ordenado en orden alfabético inverso (de la Z a la A).
"""
palabras = {"a": 5, "hola": 10, "python": 7, "programacion": 4, "es": 3, "zizizi": 11}
palabras = {palabra: valor for palabra, valor in sorted(palabras.items(), reverse=True) if len(palabra) > 3}
print(palabras)

