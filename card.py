
"""
Class Card, used to store information on a card

:arg type (int) 1 = city card from infection deck
                2 = city card from player deck
                3 = Infection card
    city (string)
    color (string)
"""
class Card:
    def __init__(self, type, city=None, color=None):
        self.type = type
        self.city = city
        self.color = color
