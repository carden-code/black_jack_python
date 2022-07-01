class Card:
    SUITS = ('♠', '♥', '♣', '♦')
    VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.values = self.find_value(rank)

    def __repr__(self):
        return f"{self.rank}{self.suite}"

    def is_ace(self):
        """Проверяет является ли карта тузом."""
        if self.rank == 'A':
            return True
        return False

    def find_value(self, rank):
        """Определяет значение для карт(картинок)."""
        if self.is_ace():
            return 11
        elif rank in ('J', 'Q', 'K'):
            return 10
        else:
            return rank
