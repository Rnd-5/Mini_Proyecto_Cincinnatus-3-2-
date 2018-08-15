import time
import os


def Presentar_Menu():
    print("╔═══════════════════════╗\n╠═Juego de Cartas 3 y 2═╣\n╚═══════════════════════╝")

    nomJ1 = input(" ◘Introduzca el nombre del jugador 1: ")
    nomJ2 = input(" ◘Introduzca el nombre del jugador 2: ")

    #print(nomJ1, nomJ2)
    time.sleep(2)


def Mostrar_Carta(numCarta=5, simbolo="♣"):
    print("╔══════╗\n║  {}   ║\n║  de  ║\n║  {}   ║\n╚══════╝".format(numCarta, simbolo))
    time.sleep(2)


def Mostrar_Mazo(cantdCart=5):
    print("╔══════╗\n"
          "║ Mazo:║\n"
          "║  {}   ║\n"
          "║cartas║\n"
          "╚══════╝".format(cantdCart))
    time.sleep(2)

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

if opcAccion == 1:
    














