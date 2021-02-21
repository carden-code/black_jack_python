from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.creates_deck_cards()
        shuffle(self.cards)

    def creates_deck_cards(self):
        suits = Card.SUITS
        values = Card.VALUES
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
