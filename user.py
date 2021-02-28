class User:
    def __init__(self, name='User'):
        self.name = name
        self.cards = []
        self.money = 100
        self.sum_cards = 0

    def place_bet_in_bank(self, bank, bet):
        if self.money >= bet:
            bank.add_money(bet)
            self.money -= bet
        else:
            raise ValueError('Не достаточно средств.')

    def take_card(self, deck):
        card = deck.deal_cards()
        self.cards.append(card)
        self.calculate_amount_points()

    def is_two_ace(self):
        if len(self.cards) == 2:
            if self.cards[0].is_ace() and self.cards[-1].is_ace():
                self.sum_cards = 21

    def calculate_amount_points(self):
        self.sum_cards = sum([card.values for card in self.cards])
        self.adjusting_card_points()

    def adjusting_card_points(self):
        if self.sum_cards > 21:
            for card in self.cards[::-1]:
                if card.is_ace():
                    self.sum_cards -= 10

