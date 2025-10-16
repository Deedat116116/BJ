from Person import Person

class BlackJack:
    def __init__(self, deck, dealer, player):
        self.perm_deck = deck
        self.deck = deck
        self.dealer = player
        self.player = dealer

    def draw(self, turn):
        if turn == 1: # Player
            card = self.deck.pop()
            if card.get_value() == 1:
                ace = input("You have drawn an ace would you like it to be an 11 or 1")
                if ace == "11":
                    card.getvalue() = 11
                else:
                    card.get_value() = 1
        else: # Dealer

    def 


    def


        