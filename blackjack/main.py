# Date: February 28, 2025

import random

VALOR_CARTAS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'AS']
VALOR_NUM_CARTAS = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 
                    10: 10, 'J': 10, 'Q': 10, 'K': 10, 'AS': 11}

def repartir_carta(mazo_cartas):
    tam_mazo = len(mazo_cartas)

    rand_index = random.randint(0, tam_mazo - 1)

    carta = mazo_cartas.pop(rand_index)
    return carta
    

def iniciar_partida():
    mazo_cartas = [carta for carta in VALOR_CARTAS for j in range(4)]

    mano_jugador = []
    mano_casa = []

    for j in range(2):
        mano_jugador.append(repartir_carta(mazo_cartas))
        mano_casa.append(repartir_carta(mazo_cartas))

    return mano_jugador, mano_casa, mazo_cartas


def suma_cartas(mano):
    suma = 0
    for carta in mano:
        suma += VALOR_NUM_CARTAS[carta]
    if 'AS' in mano:
        num_ases = sum([1 for j in mano if j == 'AS'])
        contador = 0
        while contador < num_ases and suma > 21:
            suma -= 10
            contador += 1

    return suma


def sigue_jugando(mano_jugador):
    if suma_cartas(mano_jugador) <= 21:
        return True
    return False


def determinar_ganador(mano_jugador, mano_casa):
    if (suma_cartas(mano_casa) > 21) or (suma_cartas(mano_jugador) <= 21 and suma_cartas(mano_jugador) > suma_cartas(mano_casa)):
        return 'El jugador'
    return 'La casa'


# Iniciar la partida -> Repartir mazo de cartas completo
while True:
    print('¡Bienvenido al blackjack!')
    mano_jugador, mano_casa, mazo_cartas = iniciar_partida()
    # print('')
    # print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
    # print('Cartas de la computadora: ', mano_casa, suma_cartas(mano_casa))
    # print('')

    # empieza bucle - hasta que se cumple una condición
    while sigue_jugando(mano_jugador):

        print('')
        print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
        print('Cartas de la computadora: ', mano_casa, suma_cartas(mano_casa))
        print('')

        # - Se le pregunta al jugador si pide o se planta
        print('¿Quieres Pedir (P) o Plantarse (S)?')
        condicion_pide_o_planta = (suma_cartas(mano_jugador) == 21 or 
            (suma_cartas(mano_casa) >= 17 and suma_cartas(mano_jugador) > suma_cartas(mano_casa)))
        pide_o_planta = input() if not condicion_pide_o_planta else 'S'
        #   - Si pide se le reparte una carta
        if pide_o_planta == 'P':
            mano_jugador.append(repartir_carta(mazo_cartas))
#       - Si se planta la casa se reparte a si misma hasta cumplir una condición
        elif pide_o_planta == 'S':
            while suma_cartas(mano_casa) <= 16:
                mano_casa.append(repartir_carta(mazo_cartas))
            # Se podria hacer esto pero no es una buena práctica
            break
    
    print('')
    print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
    print('Cartas de la computadora: ', mano_casa, suma_cartas(mano_casa))
    print('')


    #  Determinar el ganador
    ganador = determinar_ganador(mano_jugador, mano_casa)
    print('Ha ganado', ganador)
    break