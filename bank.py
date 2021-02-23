class Bank:
    def __init__(self):
        self.money = 0

    def add_money(self, money):
        self.money += money

    def make_payment(self, player):
        player.money += self.money
        self.money = 0
