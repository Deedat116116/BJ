"""
Filename: blackjack.py
Author: <Holtslander, Henry>
Created: <MM/DD/YYYY>
Instructor: Holtslander
"""

import pygame

class Card:
    def __init__(self, name, path, value, suit):
        """
        Class definition of a standard playing card.
        :param name: The name of the card
        :param path: The path to the file location of the card image
        :param value: Converted numerical value of the card
        :param suit: Classification of the card (Club, Diamond, Heart, Spade)
        """
        self.name = name
        self.path = path

        self.file = self.path + ".png"

        self.img = pygame.image.load(self.file)
        self.rect = self.img.get_rect(center=(500, 500))

        self.value = value
        self.suit = suit

    def get_name(self):
        """
        Getter method for card name
        :return: The name of the card as a string
        """
        return self.name

    def get_path(self):
        """
        Getter method for the path to the card image
        :return: The path to the card image as a string
        """
        return self.path

    def get_value(self):
        """
        Getter method for the converted numerical value of the card
        :return: The converted numerical value of the card as an integer
        """
        return self.value

    def get_suit(self):
        """
        Getter method for the suit of the card
        :return: The suit of the card as a string
        """
        return self.suit

    def update(self, surface):
        """
        Redraws the entity
        :param surface: The surface to draw the entity on
        """
        surface.blit(self.img, self.rect)

    def move(self, x, y):
        """
        Moves the entity to the (x,y) coordinate pair.

        :param x: The x coordinate of the center of the image
        :param y: The y coordinate of the center of the image
        """
        self.rect = self.img.get_rect(center=(x, y))