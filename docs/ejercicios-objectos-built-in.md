# Ejercicios

Aquí tienes un listado de ejercicios prácticos sobre Python, diseñados para ayudarte a fortalecer tu comprensión de los conceptos fundamentales y avanzados del lenguaje:

## Ejercicios Básicos en Python

1. Imprimir los primeros 10 números
Crea un programa que imprima los primeros 10 números naturales (1 a 10).

2. Suma de una lista de números
Dada una lista de números, escribe una función que calcule y retorne la suma de todos los elementos.

```python
numbers = [1, 2, 3, 4, 5]
Contar la cantidad de elementos en una lista
Crea un programa que reciba una lista y cuente cuántos elementos contiene.
```

3. Invertir una cadena
Escribe un programa que reciba una cadena y la imprima en orden inverso.

4. Palíndromos
Escribe una función que verifique si una palabra es un palíndromo (se lee igual al derecho que al revés).

```python
def es_palindromo(cadena):
    return cadena == cadena[::-1]
```

5. Multiplicación de dos matrices
Escribe una función que multiplique dos matrices 2x2.

6. El valor máximo y mínimo de una lista
Crea una función que reciba una lista de números y retorne el valor máximo y mínimo.

7. Verificación de un número primo
Escribe una función que reciba un número y devuelva si es primo o no.

8. Contar las vocales en una cadena
Crea una función que cuente cuántas vocales hay en una cadena de texto.

9. Generar un rango de números
Escribe un programa que genere un rango de números entre 1 y 100, pero imprima "Fizz" si el número es divisible por 3, "Buzz" si es divisible por 5 y "FizzBuzz" si es divisible por ambos.

## Ejercicios Intermedios en Python

10. Cálculo de Fibonacci
Crea una función que reciba un número n y calcule el n-ésimo número de la secuencia de Fibonacci.

11. Convertir una lista en un diccionario
Escribe una función que reciba dos listas y las combine en un diccionario, donde los elementos de la primera lista sean las claves y los de la segunda lista sean los valores.

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
```

12. Ordenar una lista de diccionarios por una clave
Dada una lista de diccionarios, escribe un programa que los ordene por una de las claves.

```python
items = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
```

13. Contar palabras en una cadena
Escribe una función que cuente cuántas veces aparece una palabra en una cadena de texto.

14. Eliminar duplicados de una lista
Crea una función que elimine los elementos duplicados de una lista y retorne una nueva lista sin duplicados.

15. Generar un diccionario con claves como números y valores como sus cuadrados
Crea un diccionario donde las claves sean los números del 1 al 10 y los valores sean sus respectivos cuadrados.

16. Crear un programa de conversión de unidades
Crea una función que convierta entre diferentes unidades de medida (por ejemplo, de metros a kilómetros, de gramos a kilogramos).

17. Contar la frecuencia de elementos en una lista
Dada una lista de elementos, escribe una función que cuente cuántas veces aparece cada elemento en la lista.

18. Filtrar palabras con más de 4 caracteres
Escribe un programa que reciba una lista de palabras y filtre aquellas que tengan más de 4 caracteres.

19. Generar una lista de números al azar
Crea una lista de 10 números aleatorios entre 1 y 100, y ordena la lista de menor a mayor.

## Ejercicios Avanzados en Python

20. Implementar una clase CuentaBancaria
Crea una clase llamada CuentaBancaria que tenga métodos para depositar dinero, retirar dinero y verificar el saldo. Asegúrate de que no se pueda retirar más dinero del que hay en la cuenta.

21. Ordenación por múltiples claves
Dada una lista de diccionarios con información de empleados, ordena la lista primero por el salario y luego por la edad.

22. Implementar un sistema de registro de usuarios
Crea un programa donde los usuarios puedan registrarse con nombre, correo electrónico y contraseña. Los usuarios deben poder iniciar sesión verificando su correo y contraseña.

23. Creación de una función de búsqueda binaria
Implementa la búsqueda binaria para encontrar un número dentro de una lista ordenada.

24. Crear un archivo CSV con datos
Escribe un programa que genere un archivo CSV con nombres, edades y ciudades de una lista de personas.

25. Simulación de un sistema de gestión de tareas
Crea una clase llamada Tarea que tenga atributos como nombre, descripción, fecha límite y estado. Además, crea una clase GestorDeTareas para gestionar una lista de tareas y permitir acciones como agregar, eliminar o marcar tareas como completadas.

26. Contador de palabras en un archivo de texto
Crea un programa que cuente cuántas veces aparece cada palabra en un archivo de texto y muestre los resultados en orden descendente.

27. Implementar una cola y una pila
Crea una clase Pila y una clase Cola para simular una estructura de datos de pila (LIFO) y cola (FIFO). Añade métodos para agregar elementos, eliminar elementos y verificar si la pila o cola están vacías.

28. Crear un generador de contraseñas aleatorias
Implementa una función que genere contraseñas aleatorias con una longitud determinada, incluyendo caracteres especiales, números y letras mayúsculas y minúsculas.

22. Simulación de un sistema de reservas de vuelos
Crea un sistema de reservas para vuelos donde los usuarios puedan reservar, cancelar y verificar el estado de sus reservas. Asegúrate de manejar casos de vuelos ya reservados y vuelos disponibles.

## Ejercicios sobre OOP en Python

23. Implementar una clase Animal y sus subclases
Crea una clase base Animal con métodos para caminar, dormir y hablar. Luego, crea subclases como Perro, Gato y Pájaro que hereden de Animal y sobrescriban el método de hablar.

24. Crear una clase Producto con descuentos
Crea una clase Producto con atributos como nombre, precio y cantidad en inventario. Añade un método para aplicar un descuento a un producto y otro para verificar si hay suficiente inventario.

25. Sistema de gestión de empleados
Crea una clase Empleado con atributos como nombre, salario, fecha de contratación y cargo. Añade métodos para calcular la antigüedad, y la clase debe incluir una subclase Gerente que tenga un método para calcular un bono.

26. Crear una clase Libro
Crea una clase Libro con atributos como título, autor, año de publicación y número de páginas. Añade un método para obtener una breve descripción del libro.

## Ejercicios sobre Manipulación de Archivos

27. Leer y escribir en un archivo de texto
Crea un programa que lea un archivo de texto línea por línea e imprima su contenido en consola. Luego, crea un archivo nuevo y escribe algunas líneas en él.

28. Contar palabras en un archivo de texto
Escribe un programa que lea un archivo de texto y cuente cuántas veces aparece cada palabra en el archivo.

29. Renombrar archivos en un directorio
Crea un script que renombre todos los archivos de un directorio agregando un prefijo a sus nombres.

30. Crear un programa para buscar una palabra en varios archivos
Escribe un programa que busque una palabra específica en todos los archivos de texto en un directorio y muestre el nombre de los archivos que contienen esa palabra.

## Ejercicios sobre Bibliotecas Externas

31. Trabajar con JSON
Crea un programa que lea un archivo JSON, modifique algún valor y guarde los cambios en un nuevo archivo.

32. Usar requests para hacer peticiones HTTP
Crea un script que haga una petición HTTP a una API pública y muestre la respuesta en formato JSON.

Estos ejercicios cubren una amplia gama de conceptos, desde lo básico hasta lo avanzado, y son útiles para mejorar tus habilidades en Python. Puedes adaptar o expandir cada uno según tu nivel y necesidades.
