# Dudas

1. Cuando agrego a un objeto una propiedad usando el operador punto. Que pasa con eso? solo esa instancia posee la propiedad? Esa propiedad esta presente durante todo el ciclo de vida del objeto?
```python
    class Persona:
        contador = 0

        def __init__(self, nombre):
            self.nombre =  nombre

    Persona.especie = 'humano'
```

2. Dado lo siguiente:
Bucle for en Combinación con enumerate()
La función enumerate() es una función incorporada de Python que agrega un contador automático a los elementos que se están iterando. Esto es útil si deseas acceder a los índices de los elementos en una lista mientras iteras sobre ellos.

```python
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```
- ¿Cómo se accede a los indices de una secuencia en Python?
- ¿Qué secuencias tienen índices internos?
