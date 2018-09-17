from Functions import *

class Game:
    def __init__(self):
        self.turn = 0
        self.gameDeck = create_deck()
        self.listPlayers = []
        self.gameStack = create_stack_card(self.gameDeck)

    def Start(self):
        display_rules()
        display_menu()
        time.sleep(2)
        self.listPlayers = create_player()
        create_set_cards(self.gameDeck, self.listPlayers)

        while self.gameDeck.cardsQuantity > 0:
            os.system('cls')
            display_menu()
            display_turn(self.listPlayers, self.turn)
            display_deck(self.gameDeck, self.gameStack)
            Menu(self.gameDeck, self.gameStack, self.listPlayers, self.turn)
            check_point(self.listPlayers, self.turn, self.gameDeck)
            if self.turn == 0:
                self.turn = 1
            else:
                self.turn = 0
        self.check_winner()

    def check_winner(self):
        os.system('cls')
        print("###--Game Over--###")
        if self.listPlayers[0].points > self.listPlayers[1].points:
            print("""
                    ◘El ganador es {} ☻ ☺ ☻ ☺!!!
                        Obtuviste {} puntos.""".format(self.listPlayers[0].name, self.listPlayers[0].points))
        elif self.listPlayers[1].points > self.listPlayers[0].points:
            print("""
                            ◘El ganador es {} ☻ ☺ ☻ ☺!!!
                                Obtuviste {} puntos.""".format(self.listPlayers[1].name, self.listPlayers[1].points))
        else:
            print("""
                                    ◘Empate☻ ☺ ☻ ☺!!!
                                  Obtuvieron {} puntos.""".format(self.listPlayers[1].points))
        input()


game = Game()

game.Start()
