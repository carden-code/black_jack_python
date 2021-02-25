class Bank:
    def __init__(self):
        self.money = 0

    def add_money(self, money):
        self.money += money

    def make_payment(self):
        money = self.money
        self.money = 0
        return money
