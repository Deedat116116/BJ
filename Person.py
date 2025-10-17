

class Person:
    def __init__(self, money = 100):
        self.cards = []
        self.cards_value = 0
        self.money = money

    def get_cards(self):
        return self.cards

    def get_value(self):
        return self.cards_value
        
    def get_money(self):
        pass

    def add_card(self,card):
        self.cards.append(card)
        self.cards_value += card.get_value()

    def add_value(self,value):
        self.cards_value += value


    def add_money(amount, self):
        self.add_money += self.money

    def reset_cards(cards_value):
        return cards_value


