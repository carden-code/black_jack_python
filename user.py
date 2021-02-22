from bank import Bank


class User:
    def __init__(self, name):
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

    def calculate_amount_points(self):
        for card in self.cards:
            self.sum_cards += card.values
