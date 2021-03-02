class TerminalInterface:
    BORDERLINE = '-' * 50
    NEWLINE = "\n" * 2

    def __init__(self, game):
        self.game = game
        self.game.start()

        print(self.NEWLINE)
        print(f'{self.game.user.name} Добро пожаловать в игру BlackJack')
        print(self.NEWLINE)

        while True:
            print(f'Банк: {self.game.bank.money}')
            print(f'Ваши деньги: {self.game.user.money}')
            print('Ваши карты:')
            print(*self.game.user.cards, f'(оч. {self.game.user.sum_cards})')

            if self.game.bank.money != 0:
                print('Карты диллера:')
                print('**** (оч. **)')
            else:
                print('Карты диллера:')
                print(*self.game.dealer.cards, f'(оч. {self.game.dealer.sum_cards})')

            if self.game.bank.money != 0:
                self.game.main_menu_items()
                menu_item = input().strip()
                winner = self.game.selected(menu_item)
                if not winner:
                    print(f'Ваши очки: {self.game.user.sum_cards}')
                    print(f'Очки диллера: {self.game.dealer.sum_cards}')
                    print(f'Ничья! Возврат ставки: {self.game.bet} у.е.')
                else:
                    print(f'{winner.name} - Победил! Выигрыш: {self.game.bet * 2} у.е.')
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
