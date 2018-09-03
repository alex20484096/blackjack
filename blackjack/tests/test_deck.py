from deck import Deck


def test_deck_instance():
    d = Deck()
    assert(isinstance(d, Deck))


def test_deck_length():
    d = Deck()
    assert(len(d) == 52)


def test_deck_reset():
    d1 = Deck()
    d2 = Deck()
    d2.reset()
    assert(d1 == d2)


def test_deck_shuffle():
    d1 = Deck()
    d2 = Deck()
    d2.shuffle()
    assert (d1 != d2)
