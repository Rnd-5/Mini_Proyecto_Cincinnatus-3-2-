import time
import os
from clases import *


# ----ESTA FUNCION CREA EL MAZO DE CARTAS QUE SE UTILIZARA DURANTE EL JUEGO----#
def Crear_Mazo():
    mazo_1 = Mazo()
    mazo_1.cartsMazo = mazo_1.Generar_Mazo()
    return mazo_1


# =============================================================================#

# ----ESTA FUNCION INSTANCIA A LOS JUAGADORES----#
def Crear_Jugadores():
    # listMisCarts = Crear_ConjuntoCarts(mazoCartas)
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador1 = Jugador(nombre, puntos=0, misCart=[])
    nombre = input(" ◘Introduzca el nombre del jugador 2: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=[])

    return [jugador1, jugador2]


# =============================================================================#


# ----ESTA FUNCION REPARTE LAS CARTAS DE LOS JUGADORES A PARTIR DEL MAZO YA CREADO----#
def Crear_ConjuntoCarts(mazoJuego, listJugadores):
    misCartas1, misCartas2 = [], []

    while len(misCartas2) < 5:
        misCartas1.append(mazoJuego.cartsMazo.pop())
        misCartas2.append(mazoJuego.cartsMazo.pop())
    listJugadores[0].misCart = misCartas1
    listJugadores[1].misCart = misCartas2
    mazoJuego.cantdCart = len(mazoJuego.cartsMazo)


"""
def Asignar_Cartas(listJugadores):
    listMisCarts = Crear_ConjuntoCarts(mazoJuego)
    listJugadores[0].misCart = listMisCarts[0]
    listJugadores[1].misCart = listMisCarts[1]
    mazoJuego.cantdCart = len(mazoJuego.cartsMazo)
"""


# =============================================================================#


# ----ESTA FUNCION INSTANCIA UNA PILA DE CARTAS----#
def Crear_PilaCart(mazoJuego):
    pila_1 = PilaCartas()
    pila_1.cartsPila.append(mazoJuego.cartsMazo.pop())
    pila_1.cantdCart = len(pila_1.cartsPila)
    return pila_1


# =============================================================================#


def Mostrar_Menu():
    print("""
            ╔═══════════════════════╗
            ╠═Juego de Cartas 3 y 2═╣
            ╚═══════════════════════╝\n""")

    # nomJ1 = input(" ◘Introduzca el nombre del jugador 1: ")
    # nomJ2 = input(" ◘Introduzca el nombre del jugador 2: ")
    # listNom = [nomJ1, nomJ2]
    # return listNom
    # return nomJ1, nomJ2
    # print(nomJ1, nomJ2)
    return
    time.sleep(2)


def Mostrar_Carta(listCartas):
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

    for carta in listCartas:
        print("     ║{} de {}║".format(carta.numCarta, carta.simbolo), end="")
    print("\n")


def Mostrar_Mazo(mazoJuego, pilaJuego):
    mazoJuego.cantdCart = len(mazoJuego.cartsMazo)
    print("""  
            ╔═══════╗          ╔═══════╗
            ║ Mazo: ║          ║   {}   ║
            ║  {}   ║          ║   de  ║
            ║cartas ║          ║   {}   ║
            ╚═══════╝          ╚═══════╝\n""".format(pilaJuego.cartsPila[-1].numCarta, len(mazoJuego.cartsMazo),
                                                pilaJuego.cartsPila[-1].simbolo))
    # time.sleep(2)


def Mostrar_Turno(listJugadores, mazoJuego, turno):
    """
    for jugador in listJugadores:
        print('[Turno del jugador: {} | Puntos: {}]'.format(jugador.nombre, jugador.puntos))
        print('[Cartas de ' + jugador.nombre + ']:')
        Mostrar_Carta(jugador.misCart)
        print('==============================')
    print(len(mazoJuego.cartsMazo))
    print('#####################################')
    """

    jugador = listJugadores[turno]
    print(' •Turno del jugador: {} | Puntos: {}'.format(jugador.nombre, jugador.puntos))
    print(' •Cartas de ' + jugador.nombre + ': \n')
    Mostrar_Carta(jugador.misCart)
    #print('==============================')

# =============================================================================#

#
# jugador1 = listJugadores[0]
# jugador2 = listJugadores[1]
#


def Start():
    turno = 0

    Mostrar_Menu()

    mazoJuego = Crear_Mazo()
    listJugadores = Crear_Jugadores()
    pilaJuego = Crear_PilaCart(mazoJuego)

    Crear_ConjuntoCarts(mazoJuego, listJugadores)
    os.system('cls')
    # Asignar_Cartas(listJugadores)
    while mazoJuego.cantdCart > 0:

        Mostrar_Menu()
        Mostrar_Turno(listJugadores, mazoJuego, turno)
        Mostrar_Mazo(mazoJuego, pilaJuego)
        input()
        Menu(mazoJuego, pilaJuego, listJugadores, turno)

# opcion = -3


def Menu(mazoJuego, pilaJuego, listJugadores, turno):
    print("""
 ╔══════════════════════════════════════════╗
 ║1-]Tomar una carta del mazo.              ║
 ║2-]Tomar la carta boca arriba(de la pila).║
 ╚══════════════════════════════════════════╝\n""")

    opcion = int(input(" ◘Que acción desea realizar? "))

    if opcion == 1:
        cart_Selecc = mazoJuego.cartsMazo.pop()
        time.sleep(1)
        print("     →Carta seleccionada: ║{} de {}║".format(cart_Selecc.numCarta, cart_Selecc.simbolo))

        desc = input(" •Deseas conservar esta carta (S/N)?: ").upper()
        if desc == 'S':
            subDesc = int(input(" •Cuál de tus cartas deseas tirar? :"))
            for carta in listJugadores[turno].misCart:
                if carta.numCarta == subDesc:
                    listJugadores[turno].misCart.remove(carta)
                    pilaJuego.cartsPila.append(carta)
                    # AGREGAR UNA CONFIRMACION QUE VERIFIQUE SI SE CUENTA CON EL NUM DE CARTA INTRODUCIDO
            listJugadores[turno].misCart.append(cart_Selecc)
        else:
            pilaJuego.cartsPila.append(cart_Selecc)
    elif opcion == 2:
        cart_Selecc = pilaJuego.cartsPila.pop()
        subDesc = int(input(" •Cuál de tus cartas deseas tirar? :"))
        for carta in listJugadores[turno].misCart:
            if carta.numCarta == subDesc:
                listJugadores[turno].misCart.remove(carta)
                pilaJuego.cartsPila.append(carta)
                # AGREGAR UNA CONFIRMACION QUE VERIFIQUE SI SE CUENTA CON EL NUM DE CARTA INTRODUCIDO
        listJugadores[turno].misCart.append(cart_Selecc)
    else:
        print(" ###-Error opcion no valida-###")
        Menu(mazoJuego, pilaJuego, listJugadores, turno)
        #os.system('cls')


Start()



