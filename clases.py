"""
class Clase_1(object):
    def __init__(self):
        self
"""


class Carta:

    def __init__(self, numCarta, simbolo, color):
        self.numCarta = numCarta
        self.simbolo = simbolo
        self.color = color


class Mazo:
    cantdCart = 52

    def __init__(self, ordeCart=[]):
        self.ordeCart = ordeCart


class Jugador:
    cantCart = 5

    def __init__(self, nombre, puntos, listCart=[]):
        self.nombre = nombre
        self.puntos = puntos
        self.listCart = listCart



"""
class Jugador_1(Jugador):

    def __init__(self, nombre, puntos, listCart):
"""