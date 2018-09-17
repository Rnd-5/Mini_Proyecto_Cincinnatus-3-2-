from Functions import *


def Start():

    display_rules()
    display_menu()
    time.sleep(2)

    turn = 0
    gameDeck = create_deck()
    listPlayers = create_player()
    gameStack = create_stack_card(gameDeck)

    create_set_cards(gameDeck, listPlayers)

    while gameDeck.cardsQuantity > 0:
        os.system('cls')
        display_rules()
        display_turn(listPlayers, turn)
        display_deck(gameDeck, gameStack)
        Menu(gameDeck, gameStack, listPlayers, turn)
        check_point(listPlayers, turn, gameDeck)

        if turn == 0:
            turn = 1
        else:
            turn = 0

    os.system('cls')
    print("###--Game Over--###")
    if listPlayers[0].points > listPlayers[1].points:
        print("""
        ◘El ganador es {} ☻ ☺ ☻ ☺!!!
            Obtuviste {} puntos.""".format(listPlayers[0].name, listPlayers[0].points))
    elif listPlayers[1].points > listPlayers[0].points:
        print("""
                ◘El ganador es {} ☻ ☺ ☻ ☺!!!
                    Obtuviste {} puntos.""".format(listPlayers[1].name, listPlayers[1].points))
    else:
        print("""
                        ◘Empate☻ ☺ ☻ ☺!!!
                      Obtuvieron {} puntos.""".format(listPlayers[1].points))
    input()


Start()
