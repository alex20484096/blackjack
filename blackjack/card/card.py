class Card(object):
    SUITS = ['Club', 'Diamond', 'Heart', 'Spade']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        '''
        Check if supplied parameters are valid before setting attributes
        '''
        if suit in self.SUITS and value in self.VALUES:
            self.suit = suit
            self.value = value
        else:
            raise ValueError

    def __str__(self):
        '''
        Nice string version of a card e.g. A of Spades
        Used when anything tries to conver the Card to a string e.g. print()
        '''
        return str(f'{self.value} of {self.suit}s')

    def __repr__(self):
        '''
        Uses __str__
        Used to represent the Card
        '''
        return self.__str__()

    def __eq__(self, other):
        '''
        Used when something trys to compare equality of a card
        One card is equal to another if they match suit and value
        '''
        try:
            return self.suit == other.suit and self.value == other.value
        except AttributeError:  # Will be raised if other is not a Card
            return False
