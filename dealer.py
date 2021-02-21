from user import User


class Dealer(User):
    def __init__(self, name='Dealer'):
        super().__init__(name)

    def take_card(self, deck):
        card = deck.deal_cards()
        self.cards.append(card)
