from random import *


class Carta:

    def __init__(self, numCarta, simbolo):
        self.numCarta = numCarta
        self.simbolo = simbolo
        # self.color = color


class Mazo:
    cantdCart = 52
    listSimbl = ['♥', '♦', '♣', '♠']

    def __init__(self, cartsMazo=[]):
        # self.ordeCart = ordeCart
        self.cartsMazo = cartsMazo

    def Generar_Mazo(self):

        for simbolo in self.listSimbl:
            for cnt in range(1, 14):
                carta = Carta(cnt, simbolo)
                # ('|', carta.numCarta, carta.simbolo, '|')
                self.cartsMazo.append(carta)
        # print('===========================')
        # self.listCartas = sample(self.listCartas, 52)
        # for carta in self.listCartas:
        #    print('|', carta.numCarta, carta.simbolo, '|')

        self.cartsMazo = sample(self.cartsMazo, 52)
        return self.cartsMazo


class Jugador:
    cantMaxCart = 5

    def __init__(self, nombre, puntos=0, misCart=[]):
        self.nombre = nombre
        self.puntos = puntos
        self.misCart = misCart


class PilaCartas:
    cantdCart = 0

    def __init__(self, cartsPila=[]):
        self.cartsPila = cartsPila




# mazo_1 = Mazo()
# u = mazo_1.Generar_Mazo()
# print(u[51].numCarta, u[50].simbolo)
# print(len(u))
