import Black_jack

class Person:
    def __init__(self):
        self.cards = []
        self.cards_value = 0

    def get_cards(self):
        return self.cards

    def get_value(self):
        return self.cards_value
        
    def get_money(self):
        return self.money

    def add_card(self,card):
        self.cards.append(card)
        self.recalculate_value()

    def recalculate_value(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')

        # Adjust Aces from 11 to 1 if total goes over 21
        while aces > 0 and total > 21:
            total -= 10
            aces -= 1

        self.cards_value = total

    def add_money(self, money):
        self.money += money

    def reset_cards(self):
        self.cards = []
        self.crads_value = 0


