from dealer import Dealer
from deck import Deck
from bank import Bank


class Game:
    BORDERLINE = '-' * 50
    NEWLINE = "\n" * 2

    def __init__(self, user):
        self.user = user
        self.dealer = Dealer()
        self.deck = Deck()
        self.bank = Bank()
        self.bet = 10

    def start(self):
        """Запрашивает имя игрока и запускает игру."""
        name = input('Введите ваше имя: ').strip()
        self.user.name = name
        self.new_round()

    def new_round(self):
        """Обновляет раунд.
            Создаёт новую колоду, обнудяет карты игроков,
            раздаёт новые карты игрокам, делает ставку и считает очки."""
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

    def new_game(self):
        """Обнуляет всё к исходному положению. И запускает игру снова."""
        self.bank.money = 0
        self.user.money = 100
        self.dealer.money = 100
        self.new_round()

    def determine_winner(self):
        """Возвращает победителя."""
        if self.user.is_two_ace() and not self.dealer.is_two_ace():
            return self.user
        if self.dealer.is_two_ace() and not self.user.is_two_ace():
            return self.dealer
        if self.user.sum_cards > 21:
            return self.dealer
        elif self.dealer.sum_cards > 21:
            return self.user
        elif self.dealer.sum_cards < self.user.sum_cards <= 21:
            return self.user
        elif self.user.sum_cards < self.dealer.sum_cards <= 21:
            return self.dealer
        elif self.user.sum_cards == self.dealer.sum_cards:
            return None

    def payout_to_winner(self):
        """Выплачивает деньги из банка победителю."""
        winner = self.determine_winner()
        bank_money = self.bank.make_payment()
        if winner:
            winner.money += bank_money
        else:
            self.user.money += bank_money // 2
            self.dealer.money += bank_money // 2

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
            if self.user.sum_cards > 21:
                self.payout_to_winner()
                return self.dealer
        elif menu_item == '2':
            while self.dealer.sum_cards <= 17:
                self.dealer.take_card(self.deck)
            winner = self.determine_winner()
            self.payout_to_winner()
            if not winner:
                return
            return winner

    def menu_2(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.BORDERLINE,
                    ' 1 - Продолжить.',
                    ' 0 - Выйти из игры.',
                    self.BORDERLINE]

        for item in messages:
            print(item)

    def selected_2(self, menu):
        if menu == '1':
            self.new_round()

    def menu_3(self):
        messages = ['Выберите действие, введя номер из списка: ',
                    self.BORDERLINE,
                    ' 1 - Новая игра.',
                    ' 0 - Выйти из игры.',
                    self.BORDERLINE]
        for item in messages:
            print(item)

    def selected_3(self, menu):
        if menu == '1':
            self.new_game()
