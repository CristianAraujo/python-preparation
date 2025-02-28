# Dudas

1. Cuando agrego a un objeto una propiedad usando el operador punto. Que pasa con eso? solo esa instancia posee la propiedad? Esa propiedad esta presente durante todo el ciclo de vida del objeto?
```python
    class Persona:
        contador = 0

        def __init__(self, nombre):
            self.nombre =  nombre

    Persona.especie = 'humano'
```