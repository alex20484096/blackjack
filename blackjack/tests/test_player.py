from player import Players
import pytest


@pytest.fixture
def player():
    return Players()
