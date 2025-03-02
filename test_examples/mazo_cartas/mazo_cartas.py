# Date: March 01, 2025

from random import shuffle, randint
from collections import namedtuple

def generar_mazo(mezclar=False):
    """Crea una baraja de cartas de tipo Carta('rank', 'suit')
       y lo devuelve mezclado si mezclar es verdadero

    Args:
        mezclar (bool, optional): mezcla aleatoriamente las cartas
        luego de crearlas

    Returns:
        List[Carta]: Retorna una baraja de cartas en forma de lista
        donde cada elemento es del tipo namedtuple y representa unaa
        carta
    """

    Carta = namedtuple('Carta', ['rank', 'suit', 'value'])

    ranks = [num for num in range(2, 11)] + ['J', 'Q', 'K', 'AS']
    suits = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    values = {'J': 10, 'Q':10, 'K': 10, 'AS': (1, 11) }

    # Generar mazo
    mazo = [
        Carta(
            rank = rank, 
            suit = suit, 
            value = rank if isinstance(rank, int) else values[rank]
        ) 
        for suit in suits 
        for rank in ranks
    ]

    # Mezclar mazo
    if mezclar: 
        shuffle(mazo)
    
    return mazo

def repartir_carta(mazo: list) -> list:
    return mazo.pop(randint(0, len(mazo) - 1))