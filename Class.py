from random import sample


class Card:
    # Esta clase representa una carta o baraja la cual posee un numero(del 1 al 13) y un simbolo(♥ ♦ ♣ ♠)
    def __init__(self, numCard, symbol):
        self.numCard = numCard
        self.symbol = symbol


class Deck:
    """
    El Deck sera el conjunto de cartas necesarios para el juego en total 52 cartas,
    La clase Deck posee 3 propiedades:
        -cardsQuantity: representara la cantidad de cartas con la que cuenta el Deck.
        -listSymbols:  es una lista de los simbolos de las cartas, esta lista se utiliza
        al momento de crear las diferentes cartas que conformaran el Deck del juego.
        -deckCards: es una lista que contendra las cartas ordenadas de manera aleatoria.
    Esta clase cuenta con un metodo que servira para generar el Deck que se utilizara durante el juego.
    """
    cardsQuantity = 52
    listSymbols = ['♥', '♦', '♣', '♠']

    def __init__(self, deckCards=[]):
        self.deckCards = deckCards

    def generate_deck(self):

        for symbol in self.listSymbols:
            for cnt in range(1, 14):
                card = Card(cnt, symbol)
                self.deckCards.append(card)
        self.deckCards = sample(self.deckCards, 52)
        return self.deckCards


class Player:
    # Esta clase representa a cada uno de los jugadores, posee un nombre, una cantidad de puntos, una lista de cartas(5 cartas)

    def __init__(self, name, points=0, myCards=[]):
        self.name = name
        self.points = points
        self.myCards = myCards


class StackCards:
    # Esta clase representa la pila de cartas que se iran desechando por los jugadores en el transcurso del juego.
    cardsQuantity = 0

    def __init__(self, cardsStack=[]):
        self.cardsStack = cardsStack
