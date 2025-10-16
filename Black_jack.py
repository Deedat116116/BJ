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
                ace = input("You have dran an ace would you like it to be an 11 or 1")
                if ace == "11":
                    self.player.add_card(card)
                    self.player.add_value(10)
                else:
                    card.get_value() = 1

        

        else: # Dealer
            

    def 


    def


        