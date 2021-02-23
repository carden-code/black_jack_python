from dealer import Dealer
from deck import Deck
from bank import Bank


class Game:
    def __init__(self, user):
        self.user = user
        self.dealer = Dealer()
        self.deck = Deck()
        self.bank = Bank()
        self.bet = 10

    def new_round(self):
        self.deck = Deck()
        self.user.cards = []
        self.dealer.cards = []
        self.user.take_card(self.deck)
        self.user.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.user.place_bet_in_bank(bank=self.bank, bet=self.bet)
        self.dealer.place_bet_in_bank(bank=self.bank, bet=self.bet)
        self.user.calculate_amount_points()
        self.dealer.calculate_amount_points()

    def determine_winner(self):
        if self.user.sum_cards > 21:
            return self.dealer
        elif self.dealer.sum_cards > 21:
            return self.user
        elif self.user.sum_cards < self.dealer.sum_cards:
            return self.dealer
        elif self.dealer.sum_cards < self.user.sum_cards:
            return self.user

    def payout_to_winner(self):
        winner = self.determine_winner()
        self.bank.make_payment(winner)
