from user import User


class Dealer(User):
    def __init__(self, name='Dealer'):
        super().__init__(name)
