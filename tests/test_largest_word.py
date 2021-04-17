import pytest

from lib.largest_word import get_largest_word

def test_get_largest_word():
    actual = get_largest_word()
    expected = "largest word"
    assert actual == expected