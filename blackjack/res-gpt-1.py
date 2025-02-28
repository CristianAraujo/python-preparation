import random

# Definir la baraja de cartas
VALORES_CARTAS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11  # El As puede ser 1 u 11
}

# Función para crear y barajar la baraja
def crear_baraja():
    baraja = list(VALORES_CARTAS.keys()) * 4  # 4 palos por cada valor
    random.shuffle(baraja)
    return baraja

# Función para calcular el valor de una mano
def calcular_valor_mano(mano):
    total = sum(VALORES_CARTAS[carta] for carta in mano)
    ases = mano.count('A')
    
    while total > 21 and ases > 0:
        total -= 10  # Convertir As de 11 a 1
        ases -= 1
    
    return total

# Función para repartir una carta
def repartir_carta(baraja):
    return baraja.pop()

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido al Blackjack!")
    
    baraja = crear_baraja()
    jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    computadora = [repartir_carta(baraja), repartir_carta(baraja)]
    
    while True:
        print(f"\nTus cartas: {jugador} (Total: {calcular_valor_mano(jugador)})")
        print(f"Carta de la computadora: [{computadora[0]}, '?']")
        
        if calcular_valor_mano(jugador) == 21:
            print("¡Blackjack! Has ganado.")
            return
        
        opcion = input("¿Quieres Pedir (P) o Plantarte (S)? ").strip().upper()
        if opcion == 'P':
            jugador.append(repartir_carta(baraja))
            if calcular_valor_mano(jugador) > 21:
                print(f"\nTus cartas: {jugador} (Total: {calcular_valor_mano(jugador)})")
                print("¡Te pasaste de 21! La casa gana.")
                return
        else:
            break
    
    print("\nTurno de la computadora...")
    while calcular_valor_mano(computadora) < 17:
        computadora.append(repartir_carta(baraja))
    
    print(f"Cartas de la computadora: {computadora} (Total: {calcular_valor_mano(computadora)})")
    
    # Determinar el ganador
    total_jugador = calcular_valor_mano(jugador)
    total_computadora = calcular_valor_mano(computadora)
    
    if total_computadora > 21 or total_jugador > total_computadora:
        print("¡Has ganado!")
    elif total_jugador < total_computadora:
        print("La casa gana.")
    else:
        print("Empate.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_blackjack()
