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
    # return nomJ1, nomJ2
    # print(nomJ1, nomJ2)
    time.sleep(2)


# ----ESTA FUNCION CREA EL MAZO DE CARTAS QUE SE UTILIZARA DURANTE EL JUEGO----#
def Crear_Mazo():
    mazo_1 = Mazo()
    return mazo_1.Generar_Mazo()


mazoCartas = Crear_Mazo()

# =============================================================================#

# ----ESTA FUNCION REPARTE LAS CARTAS DE LOS JUGADORES A PARTIR DEL MAZO YA CREADO----#
def Crear_ConjuntoCarts(mazoCartas):
    misCartas1 = []
    misCartas2 = []
    while len(misCartas2) < 5:
        misCartas1.append(mazoCartas.pop())
        misCartas2.append(mazoCartas.pop())
    return [misCartas1, misCartas2]


# =============================================================================#

# ----ESTA FUNCION INSTANCIA A LOS JUAGADORES----#
def Crear_Jugadores():
    #listMisCarts = Crear_ConjuntoCarts(mazoCartas)
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador1 = Jugador(nombre, puntos=0, misCart=[])
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=[])

    return [jugador1, jugador2]


listJugadores = Crear_Jugadores()

# =============================================================================#

def Asignar_Cartas(listJugadores):
    listMisCarts = Crear_ConjuntoCarts(mazoCartas)
    listJugadores[0].misCart = listMisCarts[0]
    listJugadores[1].misCart = listMisCarts[1]

"""
juan = listJugadores[0]
pedro = listJugadores[1]
"""

"""
listCartas = [
    {'numCarta': 5, 'simbolo': '♠'},
    {'numCarta': 3, 'simbolo': '♦'},
    {'numCarta': 11, 'simbolo': '♣'}
]"""
# print(listCartas[0]['numCarta'])
"""numCarta=5, simbolo="♣","""


def Mostrar_Carta(mazoCartas):
    """
    x = 0
    for carta in listCartas:
        #x += 1
        print("║{} de {}║".format(carta.numCarta, carta.simbolo))
    #print(x)
    #time.sleep(5)
    """
    print("║{} de {}║  ║ {} de {} ║  ║ {} de {} ║  ║ {} de {} ║  ║ {} de {} ║".format(mazoCartas[0].numCarta,
                                                                                      mazoCartas[0].simbolo,
                                                                                      mazoCartas[1].numCarta,
                                                                                      mazoCartas[1].simbolo,
                                                                                      mazoCartas[2].numCarta,
                                                                                      mazoCartas[2].simbolo,
                                                                                      mazoCartas[3].numCarta,
                                                                                      mazoCartas[3].simbolo,
                                                                                      mazoCartas[4].numCarta,
                                                                                      mazoCartas[4].simbolo))


def Mostrar_Mazo(cantdCart=5):
    print("╔══════╗\n"
          "║ Mazo:║\n"
          "║  {}   ║\n"
          "║cartas║\n"
          "╚══════╝".format(cantdCart))
    # time.sleep(2)


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
# if opcAccion == 1:


# Mostrar_Carta(listCartas)


#listMisCarts = Crear_ConjuntoCarts(mazoCartas)

pedro = listJugadores[0]
juan = listJugadores[1]

#--AQUI REPARTO LAS CARTAS--#
Asignar_Cartas(listJugadores)

print('[-1]' + pedro.nombre + ':')
Mostrar_Carta(pedro.misCart)
print('==============================')

print('[-1]' + juan.nombre + ':')
Mostrar_Carta(juan.misCart)
print('==============================')

print(len(mazoCartas))
print('#####################################')

#--AQUI REPARTO LAS CARTAS NUEVAMENTE--#
Asignar_Cartas(listJugadores)

print('[-2]' + pedro.nombre + ':')
Mostrar_Carta(pedro.misCart)
print('==============================')

print('[-2]' + juan.nombre + ':')
Mostrar_Carta(juan.misCart)
print('==============================')

print(len(mazoCartas))
print('#####################################')


input()
