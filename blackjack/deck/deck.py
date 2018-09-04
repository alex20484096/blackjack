import random
from card import Card


class Deck(list):
    '''
    The deck is essentially a list of cards so inherits from list
    '''

    def __init__(self):
        '''
        Initialise the parent list and reset the deck
        '''
        list.__init__(self)
        self.reset()

    def reset(self):
        '''
        Empty the deck and then populate with all of the possible cards
        '''
        self.clear()
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.append(Card(suit, value))

    def shuffle(self):
        '''
        Use the `shuffle` function from the `random` module to shuffle the deck
        '''
        random.shuffle(self)
