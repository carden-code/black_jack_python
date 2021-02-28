class TerminalInterface:
    BORDERLINE = '-' * 50
    NEWLINE = "\n" * 2

    def __init__(self, game):
        self.game = game
        self.game.start()

        while True:
            print(f'Банк: {self.game.bank.money}')
            print(f'Ваши деньги: {self.game.user.money}')
            print('Ваши карты:')
            print(*self.game.user.cards, f'(оч. {self.game.user.sum_cards})')

            if self.game.bank.money != 0:
                print('Карты диллера:')
                print('****')
                print('Сумма очков: **')
            else:
                print('Карты диллера:')
                print(*self.game.dealer.cards, f'(оч. {self.game.dealer.sum_cards})')

            if self.game.bank.money != 0:
                self.game.main_menu_items()
                menu_item = input().strip()
                self.game.selected(menu_item)
            elif not self.game.user.money or not self.game.dealer.money:
                self.game.menu_3()
                menu_item = input().strip()
                self.game.selected_3(menu_item)
            elif len(self.game.deck.cards) < 52:
                self.game.menu_2()
                menu_item = input().strip()
                if menu_item == '0':
                    break
                self.game.selected_2(menu_item)
