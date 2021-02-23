from dealer import Dealer
from user import User
from deck import Deck
from bank import Bank


class Game:
    def __init__(self, user):
        self.user = user
        self.dealer = Dealer()
        self.deck = Deck()
        self.bank = Bank()

    def new_round(self):
        self.deck = Deck()
        self.user.cards = []
        self.dealer.cards = []
        self.user.take_card(self.deck)
        self.user.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.user.calculate_amount_points()
        self.dealer.calculate_amount_points()

    def determine_winner(self):
