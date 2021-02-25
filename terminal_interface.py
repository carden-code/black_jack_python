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
            print('Карты диллера:')
            print(*self.game.dealer.cards, f'(оч. {self.game.dealer.sum_cards})')
            self.game.main_menu_items()
            menu_item = input()
            self.game.selected(menu_item)


