class Card:
    SUITS = ('♠', '♥', '♣', '♦')
    VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.values = self.find_value(rank)

    # Возвращает объект в понятном виде(в виде Значение Масть)
    def __repr__(self):
        return f"{self.rank}{self.suite}"

    # Проверка на туза.
    def is_ace(self):
        if self.rank == 'A':
            return True
        return False

    # Определяет значение для карт(картинок).
    def find_value(self, rank):
        if self.is_ace():
            return 11
        elif rank in ('J', 'Q', 'K'):
            return 10
        else:
            return rank
