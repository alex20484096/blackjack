from card import Card
import pytest


@pytest.fixture
def card():
    return Card('Club', 'A')


def test_card_instane(card):
    assert(isinstance(card, Card))


def test_card_error_suit():
    with pytest.raises(ValueError) as e:
        Card('Shovel', 'A')


def test_card_error_value():
    with pytest.raises(ValueError) as e:
        Card('Spade', 'C')


def test_card_suit(card):
    assert(card.suit == 'Club')


def test_card_value(card):
    assert(card.value == 'A')


def test_card_str(card):
    assert(str(card) == 'A of Clubs')


def test_card_repr(card):
    assert(repr(card) == 'A of Clubs')


def test_card_eq(card):
    other_card = Card('Club', 'A')
    assert(card == other_card)


def test_card_not_eq(card):
    other_card = Card('Club', 'K')
    assert(card != other_card)
