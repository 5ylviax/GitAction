import pytest
from analyzer import count_words, count_chars, find_most_common_word

def test_count_words():
    # empty string 
    assert count_words("") == 0
    assert count_words("Hello world") == 2
    assert count_words("One two three four") == 4
    with pytest.raises(ValueError):
        count_words(123)
        
def test_count_chars():
    assert count_chars("c") == 1
    assert count_chars("hello") == 5
    assert count_chars("") == 0
    with pytest.raises(ValueError):
        count_chars(3)

def test_find_most_common_word():
    assert find_most_common_word("apple banana apple") == "apple"
    assert find_most_common_word("one two two three three three") == "three"
    assert find_most_common_word("") == 0
    with pytest.raises(ValueError):
        find_most_common_word(456)
        