from random import shuffle
from card import Card


# Класс Deck создаёт колоду из объектов класса Card, раздаёт карты игрокам.
class Deck:
    def __init__(self):
        self.cards = []
        self.creates_deck_cards()
        shuffle(self.cards)

    # Наполняет колоду объектами карт.
    def creates_deck_cards(self):
        suits = Card.SUITS
        values = Card.VALUES
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    # Выдаёт карту из калоды.
    def deal_cards(self):
        card = self.cards.pop()
        return card
