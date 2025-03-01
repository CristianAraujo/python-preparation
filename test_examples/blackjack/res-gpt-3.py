import random
from collections import namedtuple
from itertools import cycle

# Definir la estructura de una carta usando namedtuple
Carta = namedtuple('Carta', ['valor', 'puntos'])

# Definir los valores de las cartas en una baraja estándar
VALORES_CARTAS = [
    Carta(valor=str(v), puntos=v) for v in range(2, 11)
] + [
    Carta(valor=c, puntos=10) for c in ('J', 'Q', 'K')
] + [
    Carta(valor='A', puntos=11)
]

# Función para crear una baraja mezclada y devolver un generador de cartas
def crear_baraja():
    baraja = VALORES_CARTAS * 4  # 4 palos por cada valor de carta
    random.shuffle(baraja)
    yield from baraja  # Usar un generador para extraer cartas una a una

# Función para calcular el valor total de una mano de cartas
def calcular_valor_mano(mano):
    total = sum(carta.puntos for carta in mano)
    ases = sum(1 for carta in mano if carta.valor == 'A')
    
    while total > 21 and ases > 0:
        total -= 10  # Convertir un As de 11 a 1 para evitar pasarse de 21
        ases -= 1
    
    return total

# Función para repartir cartas al jugador y a la computadora
def repartir_cartas(baraja):
    return [next(baraja) for _ in range(2)], [next(baraja) for _ in range(2)]

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido al Blackjack!")
    
    while True:  # Permitir múltiples rondas
        baraja = crear_baraja()
        jugador, computadora = repartir_cartas(baraja)
        
        while True:
            print(f"\nTus cartas: {[carta.valor for carta in jugador]} (Total: {calcular_valor_mano(jugador)})")
            print(f"Carta de la computadora: {[computadora[0].valor, '?']}")
            
            if calcular_valor_mano(jugador) == 21:
                print("¡Blackjack! Has ganado.")
                break
            
            opcion = input("¿Quieres Pedir (P) o Plantarte (S)? ").strip().upper()
            if opcion == 'P':
                jugador.append(next(baraja))
                if calcular_valor_mano(jugador) > 21:
                    print(f"\nTus cartas: {[carta.valor for carta in jugador]} (Total: {calcular_valor_mano(jugador)})")
                    print("¡Te pasaste de 21! La casa gana.")
                    break
            elif opcion == 'S':
                break
            else:
                print("Entrada no válida. Ingresa 'P' para Pedir o 'S' para Plantarte.")
        
        print("\nTurno de la computadora...")
        while calcular_valor_mano(computadora) < 17:
            computadora.append(next(baraja))
        
        print(f"Cartas de la computadora: {[carta.valor for carta in computadora]} (Total: {calcular_valor_mano(computadora)})")
        
        # Determinar el ganador
        total_jugador, total_computadora = map(calcular_valor_mano, (jugador, computadora))
        
        resultado = ("¡Has ganado!" if total_computadora > 21 or total_jugador > total_computadora else
                     "La casa gana." if total_jugador < total_computadora else "Empate.")
        print(resultado)
        
        # Preguntar si el usuario quiere jugar otra ronda
        nueva_ronda = input("\n¿Quieres jugar otra ronda? (S/N): ").strip().upper()
        if nueva_ronda != 'S':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

# Ejecutar el juego si el script es ejecutado directamente
if __name__ == "__main__":
    jugar_blackjack()
