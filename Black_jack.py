import card
from Person import Person
import card_setup

class BlackJack:
    def __init__(self, deck, dealer, player):
        self.perm_deck = deck
        self.deck = deck
        self.dealer = player
        self.player = dealer

    def draw(self, turn):
        ace =( "./cards/ace_of_spades",  "./cards/ace_of_hearts", "./cards/ace_of_diamonds", "./cards/ace_of_clubs")
        if turn == 1: # Player
            card = self.deck.pop()
            if card.get_value() == 1:
                for i in range(len(self.cards)):
                    # you can probably use the ace variable to make a code for the ace method.
                    if self.cards[i].get_value() == ace:
                        pass


                # ace = input("You have dran an ace would you like it to be an 11 or 1")
                # if ace == "11":
                #     self.player.add_card(card)
                #     self.player.add_value(10)
                # else:
                #     card.get_value() == 1


# for the dealer it may be just copy and paste of the code above for player.
        else: # Dealer
            card = self.deck.pop()
            if card.get_value() == 1:
                pass

            

    def reset(self):
        pass


    def shuffle(self):
        import random
        random.shuffle(self.deck)



    def run(self):
        pass

        