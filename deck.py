from random import shuffle
from card import Card


class Deck:
    """Класс Deck создаёт колоду из объектов класса Card, раздаёт карты игрокам."""
    def __init__(self):
        self.cards = []
        self.creates_deck_cards()
        shuffle(self.cards)

    def creates_deck_cards(self):
        """Наполняет колоду объектами карт."""
        suits = Card.SUITS
        values = Card.VALUES
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def deal_cards(self):
        """Выдаёт карту из калоды."""
        card = self.cards.pop()
        return card
