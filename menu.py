import time
import os
import clases
from clases import *

def Presentar_Menu():
    print("╔═══════════════════════╗\n╠═Juego de Cartas 3 y 2═╣\n╚═══════════════════════╝")

    nomJ1 = input(" ◘Introduzca el nombre del jugador 1: ")
    nomJ2 = input(" ◘Introduzca el nombre del jugador 2: ")
    listNom = [nomJ1, nomJ2]
    return listNom
    #return nomJ1, nomJ2
    #print(nomJ1, nomJ2)
    time.sleep(2)


def Crear_Mazo():
    mazo_1 = Mazo()
    mazo_1.cartsMazo = mazo_1.Generar_Mazo()
    return mazo_1.cartsMazo


cartsMazo = Crear_Mazo()


def Crear_ConjuntoCarts(cartsMazo):
    misCartas1 = []
    misCartas2 = []
    while len(misCartas2) < 5:
            misCartas1.append(cartsMazo.pop())
            misCartas2.append(cartsMazo.pop())
    listMisCarts = [misCartas1, misCartas2]
    return listMisCarts, cartsMazo


listMisCarts = Crear_ConjuntoCarts(cartsMazo)

print(listMisCarts)


def Crear_Jugadores():
    listMisCarts = Crear_ConjuntoCarts(cartsMazo)
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")

    jugador1 = Jugador(nombre, puntos=0, misCart=listMisCarts[0])
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=listMisCarts[1])
    listJugadores = [jugador1, jugador2]
    return listJugadores


#listJugadores = Crear_Jugadores()
#
#juan = listJugadores[0]
#pedro = listJugadores[1]


"""
cartsMazo = [
    {'numCarta': 5, 'simbolo': '♠'},
    {'numCarta': 3, 'simbolo': '♦'},
    {'numCarta': 11, 'simbolo': '♣'}
]"""
#print(cartsMazo[0]['numCarta'])
"""numCarta=5, simbolo="♣","""


def Mostrar_Carta(listMisCarts):
    """
    x = 0
    for carta in cartsMazo:
        #x += 1
        print("╔══════╗\n║  {}   ║\n║  de  ║\n║  {}   ║\n╚══════╝".format(carta.numCarta, carta.simbolo))
"""
    #print(x)
    #time.sleep(
    print("""
        ╔══════╗     ╔══════╗    ╔══════╗   ╔══════╗    ╔══════╗
        ║  {}   ║     ║  {}   ║    ║  {}   ║   ║  {}   ║    ║  {}   ║
        ║  de  ║     ║  de  ║    ║  de  ║   ║  de  ║    ║  de  ║
        ║  {}   ║     ║  {}   ║    ║  {}   ║   ║  {}   ║    ║  {}   ║
        ╚══════╝     ╚══════╝    ╚══════╝   ╚══════╝    ╚══════╝
         """.format(listMisCarts[0][0].numCarta, listMisCarts[0][1].numCarta, listMisCarts[0][2].numCarta, listMisCarts[0][3].numCarta, listMisCarts[0][4].numCarta, listMisCarts[0][0].simbolo, listMisCarts[0][1].simbolo, listMisCarts[0][2].simbolo, listMisCarts[0][3].simbolo, listMisCarts[0][4].simbolo) )
    print(len(cartsMazo))


def Mostrar_Mazo(cantdCart=5):
    print("╔══════╗\n"
          "║ Mazo:║\n"
          "║  {}   ║\n"
          "║cartas║\n"
          "╚══════╝".format(cantdCart))
    #time.sleep(2)
"""
Presentar_Menu()
os.system('cls')
Mostrar_Carta()
os.system('cls')
Mostrar_Mazo()

nombre = "Garcia"


print("Turno del juagador: {}".format(nombre))

print("1-) Tomar carta del mazo.")
print("2-) Tomar carta de la pila de cartas.")
opcAccion = input("Indique el numero de la accion que desea realizar: ")
"""
#if opcAccion == 1:

#Mostrar_Carta(cartsMazo)


Mostrar_Carta(listMisCarts[0])
print('==============================')
Mostrar_Carta(listMisCarts[1])
print('==============================')
print(len(cartsMazo))
print('==============================')
print('#####################################')
print('==============================')
Crear_ConjuntoCarts(cartsMazo)
listMisCarts = Crear_ConjuntoCarts(cartsMazo)
Mostrar_Carta(listMisCarts[0])
print('==============================')
Mostrar_Carta(listMisCarts[1])
print('==============================')
print(len(cartsMazo))

input()




