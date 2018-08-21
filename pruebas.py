from clases import *
#for x in range(1, 4):
#    print('f', end='')
#input()
#
#print([1,2,3,4][-1])
#print([1,2,3,4][len([1,2,3,4])-1])
"""
list5 = ['a', 'a', 'a', 'i', 'i']

print(list5.count('a'))
def Comprobar_Punto():
    select = list5[0]
    if 1 < list5.count(select) < 4:
        for x in list5[1:]:
            if x != select:
                if (list5.count(x) == 2 and list5.count(select) == 3) or (list5.count(x) == 3 and list5.count(select) == 2):
                    valido = True
                    print(valido)
                    break
                valido = False
                print(valido)
                break
    else:
        valido = False
        print(valido)

Comprobar_Punto()
"""

def Comprobar_Punto(listJugadores, turno):
    jugador = listJugadores[turno]
    listCartas = jugador.misCart
    select = listCartas[0]

    if 1 < listCartas.count(select) < 4:
        for carta in listCartas[1:]:
            if carta != select:
                if (listCartas.count(carta.numCarta) == 2 and listCartas.count(select.numCarta) == 3) or (listCartas.count(carta.numCarta) == 3 and listCartas.count(select.numCarta) == 2):
                    valido = True
                    jugador.puntos += 1
                    return True
                    # print(valido)
                    break
                valido = False
                # print(valido)
                break
    else:
        valido = False
        # print(valido)
""""""

k = input("Ent: ")

if k.isdigit():
    print(int(k) / 2)
    print(True)
elif type(k) != int:
    print(False)