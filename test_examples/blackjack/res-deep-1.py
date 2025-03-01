import random

def crear_baraja():
    """Crea y mezcla una baraja estándar de 52 cartas."""
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return (valores * 4)

def calcular_valor_mano(mano):
    """Calcula el valor óptimo de una mano considerando los Ases."""
    valor = 0
    ases = 0
    
    for carta in mano:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += int(carta)
    
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1
    
    return valor

def mostrar_juego(jugador, casa, mostrar_casa=False):
    """Muestra el estado actual del juego."""
    print(f"\nTus cartas: {jugador} (Valor: {calcular_valor_mano(jugador)})")
    if mostrar_casa:
        print(f"Casa: {casa} (Valor: {calcular_valor_mano(casa)})")
    else:
        print(f"Casa: [{casa[0]}, ?]")

def turno_jugador(mazo, mano_jugador, mano_casa):
    """Gestiona el turno del jugador."""
    while True:
        mostrar_juego(mano_jugador, mano_casa)
        accion = input("\n¿Pedir (P) o Plantarse (S)? ").upper()
        
        if accion == 'P':
            nueva_carta = mazo.pop()
            mano_jugador.append(nueva_carta)
            print(f"\nNueva carta: {nueva_carta}")
            
            if calcular_valor_mano(mano_jugador) > 21:
                mostrar_juego(mano_jugador, mano_casa)
                print("\n¡Te pasaste de 21! Perdiste.")
                return False
        elif accion == 'S':
            return True
        else:
            print("Opción inválida. Use P o S.")

def turno_casa(mazo, mano_casa):
    """Gestiona el turno automático de la casa."""
    while calcular_valor_mano(mano_casa) <= 16:
        nueva_carta = mazo.pop()
        mano_casa.append(nueva_carta)
        print(f"\nLa casa saca: {nueva_carta}")
    
    print("\nLa casa se planta.")
    return calcular_valor_mano(mano_casa)

def determinar_ganador(puntaje_jugador, puntaje_casa):
    """Determina el resultado final del juego."""
    if puntaje_jugador > 21:
        return "casa"
    if puntaje_casa > 21:
        return "jugador"
    if puntaje_jugador > puntaje_casa:
        return "jugador"
    return "casa"

def jugar_blackjack():
    """Función principal que ejecuta el juego."""
    print("¡Bienvenido al Blackjack!\n")
    random.seed()
    mazo = crear_baraja()
    random.shuffle(mazo)
    
    # Reparto inicial
    jugador = [mazo.pop(), mazo.pop()]
    casa = [mazo.pop(), mazo.pop()]
    
    # Turno del jugador
    if not turno_jugador(mazo, jugador, casa):
        return
    
    # Turno de la casa
    puntaje_jugador = calcular_valor_mano(jugador)
    puntaje_casa = turno_casa(mazo, casa)
    
    # Resultado final
    mostrar_juego(jugador, casa, True)
    resultado = determinar_ganador(puntaje_jugador, puntaje_casa)
    
    if resultado == "jugador":
        print("\n¡Ganaste! 🎉")
    else:
        print("\nLa casa gana. 💼")

if __name__ == "__main__":
    jugar_blackjack()