import random
from collections import namedtuple
from itertools import cycle

# Definir la baraja de cartas
Carta = namedtuple('Carta', ['valor', 'puntos'])
VALORES_CARTAS = [
    Carta(valor=str(v), puntos=v) for v in range(2, 11)
] + [
    Carta(valor=c, puntos=10) for c in ('J', 'Q', 'K')
] + [
    Carta(valor='A', puntos=11)
]

# Función para crear y barajar la baraja
def crear_baraja():
    baraja = VALORES_CARTAS * 4  # 4 palos por cada valor
    random.shuffle(baraja)
    return iter(baraja)  # Usar un generador para extraer cartas

# Función para calcular el valor de una mano
def calcular_valor_mano(mano):
    total = sum(carta.puntos for carta in mano)
    ases = sum(1 for carta in mano if carta.valor == 'A')
    
    while total > 21 and ases > 0:
        total -= 10  # Convertir As de 11 a 1
        ases -= 1
    
    return total

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido al Blackjack!")
    
    baraja = crear_baraja()
    jugador, computadora = [next(baraja) for _ in range(2)], [next(baraja) for _ in range(2)]
    
    while True:
        print(f"\nTus cartas: {[carta.valor for carta in jugador]} (Total: {calcular_valor_mano(jugador)})")
        print(f"Carta de la computadora: {[computadora[0].valor, '?']}")
        
        if calcular_valor_mano(jugador) == 21:
            print("¡Blackjack! Has ganado.")
            return
        
        opcion = input("¿Quieres Pedir (P) o Plantarte (S)? ").strip().upper()
        if opcion == 'P':
            jugador.append(next(baraja))
            if calcular_valor_mano(jugador) > 21:
                print(f"\nTus cartas: {[carta.valor for carta in jugador]} (Total: {calcular_valor_mano(jugador)})")
                print("¡Te pasaste de 21! La casa gana.")
                return
        else:
            break
    
    print("\nTurno de la computadora...")
    while calcular_valor_mano(computadora) < 17:
        computadora.append(next(baraja))
    
    print(f"Cartas de la computadora: {[carta.valor for carta in computadora]} (Total: {calcular_valor_mano(computadora)})")
    
    # Determinar el ganador
    total_jugador, total_computadora = map(calcular_valor_mano, (jugador, computadora))
    
    resultado = ("¡Has ganado!" if total_computadora > 21 or total_jugador > total_computadora else
                 "La casa gana." if total_jugador < total_computadora else "Empate.")
    print(resultado)

# Ejecutar el juego
if __name__ == "__main__":
    jugar_blackjack()