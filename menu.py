import time
import os

from clases import *


def Mostrar_Menu():
    print("╔═══════════════════════╗\n╠═Juego de Cartas 3 y 2═╣\n╚═══════════════════════╝")

    #nomJ1 = input(" ◘Introduzca el nombre del jugador 1: ")
    #nomJ2 = input(" ◘Introduzca el nombre del jugador 2: ")
    #listNom = [nomJ1, nomJ2]
    #return listNom
    # return nomJ1, nomJ2
    # print(nomJ1, nomJ2)
    return
    time.sleep(2)


# ----ESTA FUNCION CREA EL MAZO DE CARTAS QUE SE UTILIZARA DURANTE EL JUEGO----#
def Crear_Mazo():
    mazo_1 = Mazo()
    mazo_1.cartsMazo = mazo_1.Generar_Mazo()
    return mazo_1


# =============================================================================#

# ----ESTA FUNCION REPARTE LAS CARTAS DE LOS JUGADORES A PARTIR DEL MAZO YA CREADO----#
def Crear_ConjuntoCarts(mazoJuego):
    misCartas1, misCartas2 = [], []

    while len(misCartas2) < 5:
        misCartas1.append(mazoJuego.cartsMazo.pop())
        misCartas2.append(mazoJuego.cartsMazo.pop())
    return [misCartas1, misCartas2]


# =============================================================================#

# ----ESTA FUNCION INSTANCIA A LOS JUAGADORES----#
def Crear_Jugadores():
    #listMisCarts = Crear_ConjuntoCarts(mazoCartas)
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador1 = Jugador(nombre, puntos=0, misCart=[])
    nombre = input(" ◘Introduzca el nombre del jugador 2: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=[])

    return [jugador1, jugador2]

# =============================================================================#


def Asignar_Cartas(listJugadores):
    listMisCarts = Crear_ConjuntoCarts(mazoJuego)
    listJugadores[0].misCart = listMisCarts[0]
    listJugadores[1].misCart = listMisCarts[1]
    mazoJuego.cantdCart = len(mazoJuego.cartsMazo)

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


def Mostrar_Carta(mazoJuego):
    """
    x = 0
    for carta in listCartas:
        #x += 1
        print("║{} de {}║".format(carta.numCarta, carta.simbolo))
    #print(x)
    #time.sleep(5)
    """
    '''
    print("║{} de {}║  ║{} de {}║  ║{} de {}║  ║{} de {}║  ║{} de {}║".format(mazoCartas[0].numCarta,
                                                                              mazoCartas[0].simbolo,
                                                                              mazoCartas[1].numCarta,
                                                                              mazoCartas[1].simbolo,
                                                                              mazoCartas[2].numCarta,
                                                                              mazoCartas[2].simbolo,
                                                                              mazoCartas[3].numCarta,
                                                                              mazoCartas[3].simbolo,
                                                                              mazoCartas[4].numCarta,
                                                                              mazoCartas[4].simbolo))
    '''

    for carta in mazoJuego:
        print("║{} de {}║".format(carta.numCarta, carta.simbolo), end="  ")
    print("\n")


mazoJuego = Crear_Mazo()


def Mostrar_Mazo(mazoJuego):
    mazoJuego.cantdCart = len(mazoJuego.cartsMazo)
    print("╔═══════╗\n"
          "║ Mazo: ║\n"
          "║  {}   ║\n"
          "║ cartas║\n"
          "╚═══════╝".format(len(mazoJuego.cartsMazo)))
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


def Presentar(listJugadores, mazoJuego):
    for jugador in listJugadores:
        print('[Turno del jugador: {} | Puntos: {}]'.format(jugador.nombre, jugador.puntos))
        print('[Cartas de ' + jugador.nombre + ']:')
        Mostrar_Carta(jugador.misCart)
        print('==============================')

    print(len(mazoJuego.cartsMazo))
    print('#####################################')


#mazoCartas = Crear_Mazo()

listJugadores = Crear_Jugadores()
#
#jugador1 = listJugadores[0]
#jugador2 = listJugadores[1]
#
Asignar_Cartas(listJugadores)
Presentar(listJugadores, mazoJuego)
Mostrar_Mazo(mazoJuego)

Asignar_Cartas(listJugadores)
Mostrar_Mazo(mazoJuego)
print(mazoJuego.cantdCart)
#Mostrar_Menu()

input()
