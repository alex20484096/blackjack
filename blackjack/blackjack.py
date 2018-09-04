from card import Card
from deck import Deck


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    player = []
    dealer = []
    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())

    print(player)
    print(dealer)
