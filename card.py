"""
Filename: blackjack.py
Author: <Holtslander, Henry>
Created: <MM/DD/YYYY>
Instructor: Holtslander
"""


class Card:
    def __init__(self, suit, rank):
        """
        Class definition of a standard playing card.
        :param name: The name of the card
        :param path: The path to the file location of the card image
        :param value: Converted numerical value of the card
        :param suit: Classification of the card (Club, Diamond, Heart, Spade)
        """
        self.rank = rank # 2 to 10, "J", "Q","K", "A"
        self.suit = suit # 'clubs', 'dimonds', 'hearts', 'spades'

        if rank in ('J', 'Q', 'K'):
            self.value = 10
        elif rank == 'A':
            self.value = 1
        else: self.value = int(rank)


        def get_value(self):
            return self.value

        def __str__(self):
            return f"{self.rank} of {self.suit}"
