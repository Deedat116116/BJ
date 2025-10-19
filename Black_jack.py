from card import Card
import random
from Person import Person

class BlackJack:
    def __init__(self):
        self.perm_deck = self.build_deck
        self.deck = list(self.perm_deck())
        random.shuffle(self.deck)
        self.player = Person()
        self.dealer = Person()
        self.started = False

    def build_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        return [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck = list(self.perm_deck)
        random.shuffle(self.deck)
        self.player.reset_cards()
        self.dealer.reset_cards()
        self.started = False

    def _deal_to(self, person):
        if not self.deck:
            # rebuild and reshuffle if deck empties
            self.reset()
        card = self.deck.pop()
        person.add_card(card)
        return card

    def deal_initial(self):
        self.player.reset_cards()
        self.dealer.reset_cards()
        # deal: player, dealer, player, dealer
        self._deal_to(self.player)
        self._deal_to(self.dealer)
        self._deal_to(self.player)
        self._deal_to(self.dealer)
        self.started = True

    def hit_player(self):
        return self._deal_to(self.player)

    def dealer_play(self):
        # Dealer reveals and hits until 17 or more (standard rule)
        # Aces handled in Person._recalculate_value
        while self.dealer.get_value() < 17:
            self._deal_to(self.dealer)

    def get_player_cards(self):
        return self.player.get_cards()

    def get_dealer_cards(self):
        return self.dealer.get_cards()

    def get_player_value(self):
        return self.player.get_value()

    def get_dealer_value(self):
        return self.dealer.get_value()

        # THIS BIT OF CODE IS NOT ENTIRELY MINE I GOT HELP FROM CHATGPT AND YOUTUBE VIDEOS

    def show_partial(self):

        dealer_cards = self.get_dealer_cards()
        if not dealer_cards:
            dealer_str = "(no cards)"
        elif len(dealer_cards) == 1:
            dealer_str = str(dealer_cards[0])
        else:
            dealer_str = f"{dealer_cards[0]}  |  Hidden"
        player_cards = ", ".join(str(c) for c in self.get_player_cards())
        return dealer_str, player_cards

    def show_full(self):
        dealer_cards = ", ".join(str(c) for c in self.get_dealer_cards())
        player_cards = ", ".join(str(c) for c in self.get_player_cards())
        return dealer_cards, player_cards



        