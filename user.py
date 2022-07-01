class User:
    def __init__(self, name='User'):
        self.name = name
        self.cards = []
        self.money = 100
        self.sum_cards = 0

    def place_bet_in_bank(self, bank, bet):
        """Делает ставку в банк."""
        if self.money >= bet:
            bank.add_money(bet)
            self.money -= bet
        else:
            raise ValueError('Не достаточно средств.')

    def take_card(self, deck):
        """Добавляет карту в список и считает сумму очков."""
        card = deck.deal_cards()
        self.cards.append(card)
        self.calculate_amount_points()

    def is_two_ace(self):
        """Проверка на наличие 2ух тузов при раздаче."""
        if len(self.cards) != 2:
            return False
        if self.cards[0].is_ace() and self.cards[-1].is_ace():
            return True
        return False

    def calculate_amount_points(self):
        """Подсчитывает сумму очков карт на руках."""
        self.sum_cards = sum([card.values for card in self.cards])
        self.adjusting_card_points()

    def adjusting_card_points(self):
        """Проверяет наличие тузов на руках и исходя 
            из этого корректирует колличество очков."""
        if self.is_two_ace():
            self.sum_cards = 21
            return
        if self.sum_cards > 21:
            for card in self.cards[::-1]:
                if card.is_ace():
                    self.sum_cards -= 10
