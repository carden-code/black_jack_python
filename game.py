from dealer import Dealer
from deck import Deck
from bank import Bank


class Game:
    BORDERLINE = '-' * 50

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

    def main_menu_items(self):
        messages = ['Выберете действие, введя номер из списка.',
                    self.BORDERLINE,
                    '1 - Взять ещё карту.',
                    '2 - Пропустить.']
        for item in messages:
            print(item)

    def selected(self, menu_item):
        if menu_item == '1':
            self.user.take_card(self.deck)
        elif menu_item == '2':
            self.dealer.take_card(self.deck)