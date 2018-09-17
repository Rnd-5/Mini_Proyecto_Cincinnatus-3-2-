import os
import time
from Class import *


# =========================FUNCIONES_DE_CREACION===============================#

# ----ESTA FUNCION CREA EL MAZO DE CARTAS QUE SE UTILIZARA DURANTE EL JUEGO----#
def create_deck():
    deck_1 = Deck()
    deck_1.deckCards = deck_1.generate_deck()
    return deck_1

# =============================================================================#


# ----ESTA FUNCION INSTANCIA A LOS JUAGADORES----#
def create_player():
    name = input(" ◘Introduzca el nombre del jugador 1: ")
    player1 = Player(name, points=0, myCards=[])
    name = input(" ◘Introduzca el nombre del jugador 2: ")
    player2 = Player(name, points=0, myCards=[])

    return [player1, player2]

# =============================================================================#


# ----ESTA FUNCION REPARTE LAS CARTAS DE LOS JUGADORES A PARTIR DEL MAZO YA CREADO----#
def create_set_cards(gameDeck, listPlayers):
    if gameDeck.cardsQuantity > 9:
        myCards1, myCards2 = [], []

        while len(myCards2) < 5:
            myCards1.append(gameDeck.deckCards.pop())
            myCards2.append(gameDeck.deckCards.pop())
        listPlayers[0].myCards = myCards1
        listPlayers[1].myCards = myCards2
        gameDeck.cardsQuantity = len(gameDeck.deckCards)
    else:
        gameDeck.cardsQuantity = 0

# =============================================================================#


# ----ESTA FUNCION INSTANCIA UNA PILA DE CARTAS----#
def create_stack_card(gameDeck):
    stack_1 = StackCards()
    stack_1.cardsStack.append(gameDeck.deckCards.pop())
    stack_1.cardsQuantity = len(stack_1.cardsStack)
    return stack_1

# =============================================================================#



# =======================FUNCIONES_DE_PRESENTACION=============================#
def display_rules():
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


def display_menu():
    print("""
            ╔═══════════════════════╗
            ╠═Juego de Cartas 3 y 2═╣
            ╚═══════════════════════╝\n\n""")


def display_card(listCards):

    for card in listCards:
        print("     ║{} de {}║".format(card.numCard, card.symbol), end="")
    print("\n")


def display_deck(gameDeck, gameStack):
    gameDeck.cardsQuantity = len(gameDeck.deckCards)
    print("""  
            ╔═══════╗          ╔═══════╗
            ║ Mazo: ║          ║   {}   ║
            ║  {}   ║          ║   de  ║
            ║cartas ║          ║   {}   ║
            ╚═══════╝          ╚═══════╝\n""".format(gameStack.cardsStack[-1].numCard, len(gameDeck.deckCards),
                                                     gameStack.cardsStack[-1].symbol))


def display_turn(listPlayers, turn):

    player = listPlayers[turn]
    print(' •Turno del jugador: {} | Puntos: {}'.format(player.name, player.points))
    print('\n •Cartas de ' + player.name + ': -→', end="")
    display_card(player.myCards)


def Menu(gameDeck, gameStack, listPlayers, turn):
    print("""
 ╔══════════════════════════════════════════╗
 ║1-]Tomar una carta del mazo.              ║
 ║2-]Tomar la carta boca arriba(de la pila).║
 ╚══════════════════════════════════════════╝\n""")

    option = input(" ◘Que acción desea realizar? ")

    if option.isdigit():
        option = int(option)

        if option == 1:
            if gameDeck.cardsQuantity > 0:
                cardSelected = gameDeck.deckCards.pop()
                time.sleep(1)
                print("     →Carta seleccionada: ║{} de {}║".format(cardSelected.numCard, cardSelected.symbol))
                while True:
                    desc = input(" •Deseas conservar esta carta (S/N)?: ").upper()
                    if desc == 'S':
                        while True:
                            subDesc = input(" •Cuál de tus cartas deseas tirar? :")
                            if subDesc.isdigit():
                                subDesc = int(subDesc)
                                listElemts = []
                                for elemt in listPlayers[turn].myCards:
                                    listElemts.append(elemt.numCard)

                                if subDesc in listElemts:

                                    for card in listPlayers[turn].myCards:
                                        if card.numCard == subDesc:
                                            listPlayers[turn].myCards.remove(card)
                                            gameStack.cardsStack.append(card)
                                            break
                                    listPlayers[turn].myCards.append(cardSelected)
                                    break
                                print(" ##-No cuentas con la carta que has indicado-##")
                                input("    →Presiona [ENTER] para continuar")
                            else:
                                print(" ##-Debes introducir el numero de unas de tus cartas-##")
                                input("    →Presiona [ENTER] para continuar")
                        break
                    elif desc == 'N':
                        gameStack.cardsStack.append(cardSelected)
                        break
            else:
                print("     →Ya no quedan cartas en el mazo.")
        elif option == 2:
            cardSelected = gameStack.cardsStack.pop()

            while True:
                subDesc = input(" •Cuál de tus cartas deseas tirar? :")
                if subDesc.isdigit():
                    subDesc = int(subDesc)
                    listElemts = []
                    for elemt in listPlayers[turn].myCards:
                        listElemts.append(elemt.numCard)

                    if subDesc in listElemts:
                        for card in listPlayers[turn].myCards:
                            if card.numCard == subDesc:
                                listPlayers[turn].myCards.remove(card)
                                gameStack.cardsStack.append(card)
                                break
                        listPlayers[turn].myCards.append(cardSelected)
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
            display_menu()
            display_turn(listPlayers, turn)
            display_deck(gameDeck, gameStack)
            Menu(gameDeck, gameStack, listPlayers, turn)
    else:
        os.system('cls')
        print(" ###-Error opcion no valida-###")
        input()
        os.system('cls')
        display_menu()
        display_turn(listPlayers, turn)
        display_deck(gameDeck, gameStack)
        Menu(gameDeck, gameStack, listPlayers, turn)


def check_point(listPlayers, turn, gameDeck):
    player = listPlayers[turn]
    listCards = []

    for element in player.myCards:
        listCards.append(element.numCard)

    selected = listCards[0]

    if 1 < listCards.count(selected) < 4:
        for card in listCards[1:]:
            if card != selected:
                if (listCards.count(card) == 2 and listCards.count(selected) == 3) or (
                        listCards.count(card) == 3 and listCards.count(selected) == 2):
                    player.points += 1
                    os.system('cls')
                    print(" ###-{} ha ganado un punto-###".format(player.name))
                    time.sleep(2)
                    os.system('cls')
                    create_set_cards(gameDeck, listCards)
                    break
                break

# =============================================================================#
