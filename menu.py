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

mazo_1 = Mazo()
listCartas = mazo_1.Generar_Mazo()

misCartas1 = []
misCartas2 = []

while len(misCartas1) < 6:
        misCartas1.append(listCartas.pop())
        misCartas2.append(listCartas.pop())
print(misCartas1, misCartas2)


def Crear_Juagadores():
    nombre = input(" ◘Introduzca el nombre del jugador 1: ")
    jugador1 = Jugador(nombre=nombre, 0, )

"""
listCartas = [
    {'numCarta': 5, 'simbolo': '♠'},
    {'numCarta': 3, 'simbolo': '♦'},
    {'numCarta': 11, 'simbolo': '♣'}
]"""
#print(listCartas[0]['numCarta'])
"""numCarta=5, simbolo="♣","""




def Mostrar_Carta(listCartas):
    x = 0
    for carta in listCartas:
        #x += 1
        print("╔══════╗\n║  {}   ║\n║  de  ║\n║  {}   ║\n╚══════╝".format(carta.numCarta, carta.simbolo))
    #print(x)
    time.sleep(5)


def Mostrar_Mazo(cantdCart=5):
    print("╔══════╗\n"
          "║ Mazo:║\n"
          "║  {}   ║\n"
          "║cartas║\n"
          "╚══════╝".format(cantdCart))
    time.sleep(2)
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









