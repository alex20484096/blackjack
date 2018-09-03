import random
from card import Card


class Deck(list):
    def __init__(self):
        list.__init__(self)
        self.reset()

    def reset(self):
        self.clear()
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self)
