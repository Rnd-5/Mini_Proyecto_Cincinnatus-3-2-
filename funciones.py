import os
import time
from clases import *


# =========================FUNCIONES_DE_CREACION===============================#

# ----ESTA FUNCION CREA EL MAZO DE CARTAS QUE SE UTILIZARA DURANTE EL JUEGO----#
def Crear_Mazo():
    mazo_1 = Mazo()
    mazo_1.cartsMazo = mazo_1.Generar_Mazo()
    return mazo_1

# =============================================================================#


# ----ESTA FUNCION INSTANCIA A LOS JUAGADORES----#
def Crear_Jugadores():
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador1 = Jugador(nombre, puntos=0, misCart=[])
    nombre = input(" ◘Introduzca el nombre del jugador 2: ")
    jugador2 = Jugador(nombre, puntos=0, misCart=[])

    return [jugador1, jugador2]

# =============================================================================#


# ----ESTA FUNCION REPARTE LAS CARTAS DE LOS JUGADORES A PARTIR DEL MAZO YA CREADO----#
def Crear_ConjuntoCarts(mazoJuego, listJugadores):
    if mazoJuego.cantdCart > 9:
        misCartas1, misCartas2 = [], []

        while len(misCartas2) < 5:
                misCartas1.append(mazoJuego.cartsMazo.pop())
                misCartas2.append(mazoJuego.cartsMazo.pop())
        listJugadores[0].misCart = misCartas1
        listJugadores[1].misCart = misCartas2
        mazoJuego.cantdCart = len(mazoJuego.cartsMazo)
    else:
        mazoJuego.cantdCart = 0

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



# =======================FUNCIONES_DE_PRESENTACION=============================#
def Mostrar_Reglas():
    print("""
    ╔════════════════════════════════════════════════════════════════════════════════════╗
    ╠═-------------------------Este es el juego de Cartas 3 y 2-------------------------═╣
    ╠════════════════════════════════════════════════════════════════════════════════════╣
    ║ 1-]Consta de dos jugadores a los cuales se le reparten 5 cartas(a cada jugador).   ║
    ║                                                                                    ║
    ║ 2-]Un jugador ganará un punto cuando logre tener a mano 3 cartas con el mismo      ║
    ║    valor numérico y 2 cartas con otro valor numerico(mismos).                      ║
    ║    Ejemplo: tres cartas con el #6 y dos cartas con el #11.                         ║
    ║                                                                                    ║
    ║ 3-]El juego terminará hasta que no queden mas cartas en el mazo, y ganará el       ║
    ║    jugador con mayor puntos acumulados.                                            ║
    ╚════════════════════════════════════════════════════════════════════════════════════╝""")
    input("     → Presisone la tecla [ENTER] para continuar.")
    os.system('cls')


def Mostrar_Menu():
    print("""
            ╔═══════════════════════╗
            ╠═Juego de Cartas 3 y 2═╣
            ╚═══════════════════════╝\n\n""")


def Mostrar_Carta(listCartas):

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


def Mostrar_Turno(listJugadores, turno):

    jugador = listJugadores[turno]
    print(' •Turno del jugador: {} | Puntos: {}'.format(jugador.nombre, jugador.puntos))
    print('\n •Cartas de ' + jugador.nombre + ': -→', end="")
    Mostrar_Carta(jugador.misCart)


def Menu(mazoJuego, pilaJuego, listJugadores, turno):
    print("""
 ╔══════════════════════════════════════════╗
 ║1-]Tomar una carta del mazo.              ║
 ║2-]Tomar la carta boca arriba(de la pila).║
 ╚══════════════════════════════════════════╝\n""")

    opcion = input(" ◘Que acción desea realizar? ")

    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 1:
            if mazoJuego.cantdCart > 0:
                cart_Selecc = mazoJuego.cartsMazo.pop()
                time.sleep(1)
                print("     →Carta seleccionada: ║{} de {}║".format(cart_Selecc.numCarta, cart_Selecc.simbolo))
                while True:
                    desc = input(" •Deseas conservar esta carta (S/N)?: ").upper()
                    if desc == 'S':
                        while True:
                            subDesc = input(" •Cuál de tus cartas deseas tirar? :")
                            if subDesc.isdigit():
                                subDesc = int(subDesc)
                                # AGREGAR UNA CONFIRMACION QUE VERIFIQUE SI SE CUENTA CON EL NUM DE CARTA INTRODUCIDO
                                listElemt = []
                                for elemt in listJugadores[turno].misCart:
                                    listElemt.append(elemt.numCarta)

                                if subDesc in listElemt:

                                    for carta in listJugadores[turno].misCart:
                                        if carta.numCarta == subDesc:
                                            listJugadores[turno].misCart.remove(carta)
                                            pilaJuego.cartsPila.append(carta)
                                            break
                                    listJugadores[turno].misCart.append(cart_Selecc)
                                    break
                                print(" ##-No cuentas con la carta que has indicado-##")
                                input("    →Presiona [ENTER] para continuar")
                            else:
                                print(" ##-Debes introducir el numero de unas de tus cartas-##")
                                input("    →Presiona [ENTER] para continuar")
                        break
                    elif desc == 'N':
                        pilaJuego.cartsPila.append(cart_Selecc)
                        break
            else:
                print("     →Ya no quedan cartas en el mazo.")
        elif opcion == 2:
            cart_Selecc = pilaJuego.cartsPila.pop()

            while True:
                subDesc = input(" •Cuál de tus cartas deseas tirar? :")
                if subDesc.isdigit():
                    subDesc = int(subDesc)
                    # AGREGAR UNA CONFIRMACION QUE VERIFIQUE SI SE CUENTA CON EL NUM DE CARTA INTRODUCIDO
                    listElemt = []
                    for elemt in listJugadores[turno].misCart:
                        listElemt.append(elemt.numCarta)

                    if subDesc in listElemt:
                        for carta in listJugadores[turno].misCart:
                            if carta.numCarta == subDesc:
                                listJugadores[turno].misCart.remove(carta)
                                pilaJuego.cartsPila.append(carta)
                                break
                        listJugadores[turno].misCart.append(cart_Selecc)
                        break
                    print(" ##-No cuentas con la carta que has indicado-##")
                    input("    →Presiona [ENTER] para continuar")
                else:
                    print(" ##-Debes introducir el numero de unas de tus cartas-##")
                    input("    →Presiona [ENTER] para continuar")
        else:
            os.system('cls')
            print(" ###-Error opcion no valida-###")
            input()
            os.system('cls')
            Mostrar_Menu()
            Mostrar_Turno(listJugadores, turno)
            Mostrar_Mazo(mazoJuego, pilaJuego)
            Menu(mazoJuego, pilaJuego, listJugadores, turno)
    else:
        os.system('cls')
        print(" ###-Error opcion no valida-###")
        input()
        os.system('cls')
        Mostrar_Menu()
        Mostrar_Turno(listJugadores, turno)
        Mostrar_Mazo(mazoJuego, pilaJuego)
        Menu(mazoJuego, pilaJuego, listJugadores, turno)


def Comprobar_Punto(listJugadores, turno, mazoJuego):
    jugador = listJugadores[turno]
    listCartas = []

    for element in jugador.misCart:
        listCartas.append(element.numCarta)

    select = listCartas[0]

    if 1 < listCartas.count(select) < 4:
        for carta in listCartas[1:]:
            if carta != select:
                if (listCartas.count(carta) == 2 and listCartas.count(select) == 3) or (
                        listCartas.count(carta) == 3 and listCartas.count(select) == 2):
                    jugador.puntos += 1
                    os.system('cls')
                    print(" ###-{} ha ganado un punto-###".format(jugador.nombre))
                    #input()
                    time.sleep(2)
                    os.system('cls')
                    Crear_ConjuntoCarts(mazoJuego, listJugadores)
                    break
                break

# =============================================================================#
