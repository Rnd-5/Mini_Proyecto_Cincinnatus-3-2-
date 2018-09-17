from random import sample


class Card:

    def __init__(self, numCard, symbol):
        self.numCard = numCard
        self.symbol = symbol


class Deck:
    cardsQuantity = 52
    listSimbols = ['♥', '♦', '♣', '♠']

    def __init__(self, deckCards=[]):
        self.deckCards = deckCards

    def generate_deck(self):

        for symbol in self.listSimbols:
            for cnt in range(1, 14):
                card = Card(cnt, symbol)
                self.deckCards.append(card)
        self.deckCards = sample(self.deckCards, 52)
        return self.deckCards


class Player:
    cantMaxCart = 5

    def __init__(self, name, points=0, myCards=[]):
        self.name = name
        self.points = points
        self.myCards = myCards


class StackCards:
    cardsQuantity = 0

    def __init__(self, cardsStack=[]):
        self.cardsStack = cardsStack
