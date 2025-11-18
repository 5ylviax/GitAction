import pytest
from analyzer import count_words, count_chars, find_most_common_word

def count_words():
    # empty string 
    assert count_words("") == ""

    with pytest.raise(ValueError)
        assert count_words(3) == 3

def count_chars():
    assert count_words('c') == 'c'

    with pytest.raise("ValueError"):
        count_words(3)

def find_most_common_word():
    assert find_most_common_word()