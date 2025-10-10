

class Person:
    def __init__(money = 100):
        self.cards = []
        self.cards_value = 0
        self.money = money

    def get_cards():
        return self.cards

    def get_value():
        return self.cards_value
        
    def get_money():
        pass

    def add_card(card):
        self.cards.append(card)
        self.cards_value += card.get_value()

    def add_money(amount):
        self.add_money += self.money

    def reset_cards():
        return cards_value


