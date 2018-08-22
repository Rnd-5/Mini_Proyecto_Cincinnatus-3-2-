"""
class Clase_1(object):
    def __init__(self):
        self
"""
from random import *


class Carta:

    def __init__(self, numCarta, simbolo):
        self.numCarta = numCarta
        self.simbolo = simbolo
        # self.color = color


class Mazo:
    cantdCart = 52
    listSimbl = ['♥', '♦', '♣', '♠']

    def __init__(self, listCartas=[]):
        # self.ordeCart = ordeCart
        self.listCartas = listCartas

    def Generar_Mazo(self):

        for simbolo in self.listSimbl:
            for cnt in range(1, 14):
                carta = Carta(cnt, simbolo)
                # ('|', carta.numCarta, carta.simbolo, '|')
                self.listCartas.append(carta)
        # print('===========================')
        # self.listCartas = sample(self.listCartas, 52)
        # for carta in self.listCartas:
        #    print('|', carta.numCarta, carta.simbolo, '|')
        return sample(self.listCartas, 52)


class Jugador:
    cantMaxCart = 5

    def __init__(self, nombre, puntos=0, misCart=[]):
        self.nombre = nombre
        self.puntos = puntos
        self.misCart = misCart


"""
class Jugador_1(Jugador):

    def __init__(self, nombre, puntos, listCart):
"""

# mazo_1 = Mazo()
# u = mazo_1.Generar_Mazo()
# print(u[51].numCarta, u[50].simbolo)
# print(len(u))
