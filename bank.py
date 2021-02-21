class Bank:
    money = 0

    @classmethod
    def add_money(cls, money):
        cls.money += money
