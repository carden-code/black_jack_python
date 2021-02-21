from user import User
from deck import Deck


class Dealer(User):
    def __init__(self, name='Dealer'):
        super().__init__(name)

    # def take_card(self):
    #     deck = Deck.deal_cards()
    #     self.cards.append(deck)
