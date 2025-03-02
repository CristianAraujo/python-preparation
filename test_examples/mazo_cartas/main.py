import mazo_cartas
from pprint import pprint as pp

cartas = [0, []]
mazo = mazo_cartas.generar_mazo(True)
print(len(mazo))

carta = mazo_cartas.repartir_carta(mazo)
print(len(mazo))
print(carta)
cartas[0] += carta.value
cartas[1].append(carta)
pp(cartas)

carta = mazo_cartas.repartir_carta(mazo)
print(len(mazo))
print(carta)
cartas[0] += carta.value if isinstance(carta.value, int) else carta.value[1]
cartas[1].append(carta)
pp(cartas)
