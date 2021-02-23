class TerminalInterface:
    BORDERLINE = '-' * 50
    NEWLINE = "\n" * 2

    def __init__(self, game):
        self.game = game
        self.start()

    def start(self):
        name = input('Введите ваше имя: ').strip()
        self.game.user.name = name
        self.start_game()

    def start_game(self):
        self.game.new_round()
        print(self.NEWLINE)
        print(f'{self.game.user.name} Добро пожаловать в игру BlackJack')
        print(self.NEWLINE)

        while True:
            print(f'Банк: {self.game.bank.money}')
            print(f'Ваши деньги: {self.game.user.money}')
            print(f'Ваши карты: {self.game.user.cards}')
