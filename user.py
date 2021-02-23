from bank import Bank


class User:
    def __init__(self, name='User'):
        self.name = name
        self.cards = []
        self.money = 100
        self.sum_cards = 0

    def place_bet_in_bank(self):
        bet = 10
        if self.money >= bet:
            Bank.add_money(bet)
            self.money -= bet
        else:
            raise ValueError('Не достаточно средств.')

    def take_card(self, deck):
        card = deck.deal_cards()
        self.cards.append(card)
        self.calculate_amount_points()

    def calculate_amount_points(self):
        self.sum_cards = sum([card.values for card in self.cards])
        self.adjusting_card_points()

    def adjusting_card_points(self):
        if self.sum_cards > 21:
            for card in self.cards[::-1]:
                if card.is_ace():
                    self.sum_cards -= 10

