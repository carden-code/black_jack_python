from user import User
from game import Game
from terminal_interface import TerminalInterface


class BlackJack:
    def __init__(self):
        self.user = User()
        self.game = Game(self.user)
        TerminalInterface(self.game)


BlackJack()