"""
Ejercicio 3: Longitud de Palabras
Enunciado:
Dada la lista 

palabras = ["python", "diccionario", "comprensión", "ejercicio"] 

crea un diccionario donde la clave sea la palabra y el valor sea 
la cantidad de caracteres que tiene.

Solución Esperada:
{"python": 6, "diccionario": 11, "comprensión": 12, "ejercicio": 9}
"""
palabras = ["python", "diccionario", "comprensión", "ejercicio", "hi", "hola"] 
num_caracteres = { palabra: len(palabra) for palabra in palabras }
print(num_caracteres)