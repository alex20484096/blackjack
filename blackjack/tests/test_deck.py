from deck import Deck
import pytest


@pytest.fixture
def deck():
    return Deck()


def test_deck_instance(deck):
    assert(isinstance(deck, Deck))


def test_deck_length(deck):
    assert(len(deck) == 52)


def test_deck_reset(deck):
    other_deck = Deck()
    other_deck.reset()
    assert(deck == other_deck)


def test_deck_shuffle(deck):
    other_deck = Deck()
    other_deck.shuffle()
    assert (deck != other_deck)
