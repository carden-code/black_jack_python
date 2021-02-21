from bank import Bank


class User:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 100

    def place_bet_in_bank(self):
        bet = 10
        if self.money >= bet:
            Bank.add_money(bet)
            self.money -= bet
        else:
            raise ValueError('Не достаточно средств.')
