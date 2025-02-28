 # Desafío Avanzado de Programación en Python para Desarrolladores Junior

Problema:

Desarrolla un programa en Python que simule un juego de blackjack (también conocido como 21). El juego debe funcionar de la siguiente manera:

1. El programa debe permitir que un jugador juegue contra la computadora (la casa).

2. Cada jugador comienza con dos cartas. Las cartas se eligen al azar de una baraja estándar de 52 cartas (sin considerar los comodines).

3. El objetivo del juego es obtener una mano con un valor lo más cercano posible a 21 sin pasarse.

4. Las cartas numéricas (2 al 10) tienen el valor que indican. Las cartas J, Q y K valen cada una 10 puntos. El As puede valer 1 u 11 puntos, dependiendo de qué opción sea más ventajosa para el jugador.

5. Después de recibir sus dos cartas iniciales, el jugador puede elegir entre "Pedir" (recibir una carta adicional) o "Plantarse" (mantener su mano actual).

6. Si el jugador decide pedir una carta adicional y su mano supera los 21 puntos, el jugador pierde automáticamente.

7. Después de que el jugador se plante, es el turno de la computadora. La computadora debe seguir un conjunto de reglas predefinidas: debe pedir una carta adicional si su mano es menor o igual a 16 y plantarse si su mano es igual o mayor a 17.

8. Una vez que tanto el jugador como la computadora se hayan plantado, se determina el ganador. El jugador gana si su mano tiene un valor más alto que el de la computadora sin superar 21, o si la computadora se pasa de 21. La computadora gana en todos los demás casos.

Requisitos:

* El programa debe mostrar las cartas del jugador y de la computadora en cada paso del juego.

* Debes manejar correctamente el valor del As, es decir, determinar si debe contar como 1 u 11 puntos en función de la situación.

* Debes utilizar funciones para organizar tu código. Cada parte importante del juego (iniciar juego, recibir cartas, determinar ganador, etc.) debe implementarse como una función separada.

* Puedes hacer uso de bibliotecas estándar de Python si lo consideras necesario.

Ejemplo de Entrada/Salida:

```bash
¡Bienvenido al Blackjack!

Tus cartas: [8, 'A']
Carta de la computadora: [9, '?']

¿Quieres Pedir (P) o Plantarte (S)? P

Tus cartas: [8, 'A', 5]
Carta de la computadora: [9, '?']

¿Quieres Pedir (P) o Plantarte (S)? P

Tus cartas: [8, 'A', 5, 10]
Carta de la computadora: [9, '?']
```

Notas:

* Asegúrate de que tu código sea legible y esté bien comentado.

* Puedes agregar funcionalidades adicionales como la posibilidad de jugar múltiples rondas, llevar un registro de la puntuación, etc