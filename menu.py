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
    listCartas = mazo_1.Generar_Mazo()
    return listCartas


listCartas = Crear_Mazo()


def Crear_ConjuntoCarts(listCartas):
    misCartas1 = []
    misCartas2 = []
    while len(misCartas2) < 5:
            misCartas1.append(listCartas.pop())
            misCartas2.append(listCartas.pop())
    listMisCarts = [misCartas1, misCartas2]
    return listMisCarts


listMisCarts = Crear_ConjuntoCarts(listCartas)


"""
def Crear_Jugadores():
    listMisCarts = Crear_ConjuntoCarts(listCartas)
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")

    jugador1 = Jugador(nombre, puntos=0, misCart=listMisCarts[0])
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=listMisCarts[1])
    listJugadores = [jugador1, jugador2]
    return listJugadores


listJugadores = Crear_Jugadores()

juan = listJugadores[0]
pedro = listJugadores[1]
"""

"""
listCartas = [
    {'numCarta': 5, 'simbolo': '♠'},
    {'numCarta': 3, 'simbolo': '♦'},
    {'numCarta': 11, 'simbolo': '♣'}
]"""
#print(listCartas[0]['numCarta'])
"""numCarta=5, simbolo="♣","""




def Mostrar_Carta(listCartas):
    """
    x = 0
    for carta in listCartas:
        #x += 1
        print("║{} de {}║".format(carta.numCarta, carta.simbolo))
    #print(x)
    #time.sleep(5)
    """
    print("║{} de {}║  ║ {} de {} ║  ║ {} de {} ║  ║ {} de {} ║  ║ {} de {} ║".format(listCartas[0].numCarta, listCartas[0].simbolo,
                                                                                      listCartas[1].numCarta, listCartas[1].simbolo,
                                                                                      listCartas[2].numCarta, listCartas[2].simbolo,
                                                                                      listCartas[3].numCarta, listCartas[3].simbolo,
                                                                                      listCartas[4].numCarta, listCartas[4].simbolo))


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


#Mostrar_Carta(listCartas)


Mostrar_Carta(listMisCarts[0])
print('==============================')

Mostrar_Carta(listMisCarts[1])
print('==============================')
print(len(listCartas))
print('==============================')
print('#####################################')
print('==============================')

""" 
Crear_ConjuntoCarts(listCartas)
listMisCarts = Crear_ConjuntoCarts(listCartas)
Mostrar_Carta(listMisCarts[0])
print('==============================')
Mostrar_Carta(listMisCarts[1])
print('==============================')
print(len(listCartas))
"""
input()




