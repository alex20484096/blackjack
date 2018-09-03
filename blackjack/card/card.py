

class Card(object):
    SUITS = ['Club', 'Diamond', 'Heart', 'Spade']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        if suit in self.SUITS and value in self.VALUES:
            self.suit = suit
            self.value = value
        else:
            raise ValueError

    def __str__(self):
        return str(f'{self.value} of {self.suit}s')

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value
