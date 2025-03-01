# Date: March 01, 2025

"""
Ejercicio 5: Filtrado, transformación y ordenación combinados
Enunciado:
Dada la lista de tuplas con países y capitales:

paises = [("Argentina", "Buenos Aires"), ("Brasil", "Brasilia"), ("Chile", "Santiago"), ("Uruguay", "Montevideo")]
Crea un diccionario que tenga como claves las capitales y como valores 
los países, pero solo incluye aquellos países que comiencen con "A" o "B". Además, ordena el diccionario por las capitales en orden alfabético inverso.
"""
paises = [("Argentina", "Buenos Aires"), ("Brasil", "Brasilia"), ("Chile", "Santiago"), ("Uruguay", "Montevideo")]
paises = {capital: pais 
          for pais, capital
          in sorted(paises, key=lambda x: x[1], reverse=True) 
          if pais.startswith('A') or pais.startswith('B')}
print(paises)