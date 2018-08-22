from funciones import *


def Iniciar():

    Mostrar_Reglas()
    Mostrar_Menu()
    time.sleep(2)

    turno = 0
    mazoJuego = Crear_Mazo()
    listJugadores = Crear_Jugadores()
    pilaJuego = Crear_PilaCart(mazoJuego)

    Crear_ConjuntoCarts(mazoJuego, listJugadores)

    while mazoJuego.cantdCart > 0:
        os.system('cls')
        Mostrar_Menu()
        Mostrar_Turno(listJugadores, turno)
        Mostrar_Mazo(mazoJuego, pilaJuego)
        #input(" •Presione la tecla [ENTER] ")
        Menu(mazoJuego, pilaJuego, listJugadores, turno)
        Comprobar_Punto(listJugadores, turno, mazoJuego)

        if turno == 0:
            turno = 1
        else:
            turno = 0

    os.system('cls')
    print("###--Game Over--###")
    if listJugadores[0].puntos > listJugadores[1].puntos:
        print("""
        ◘El ganador es {} ☻ ☺ ☻ ☺!!!
            Obtuviste {} puntos.""".format(listJugadores[0].nombre, listJugadores[0].puntos))
    elif listJugadores[1].puntos > listJugadores[0].puntos:
        print("""
                ◘El ganador es {} ☻ ☺ ☻ ☺!!!
                    Obtuviste {} puntos.""".format(listJugadores[1].nombre, listJugadores[1].puntos))
    else:
        print("""
                        ◘Empate☻ ☺ ☻ ☺!!!
                      Obtuvieron {} puntos.""".format(listJugadores[1].puntos))
    input()


Iniciar()
