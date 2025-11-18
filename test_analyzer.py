import pytest
from analyzer import count_words, count_chars, find_most_common_word

def count_words():
    # empty string 
    assert count_words("") is None
    assert count_words("Hello world") == "Hello world"
    assert count_words("One two three four") == "One two three four"
    with pytest.raises(ValueError):
        count_words(123)
        
def count_chars():
    assert count_chars('c') == 'c'
    assert count_chars('hello') == 'hello'
    with pytest.raises(ValueError):
        count_chars(3)

def find_most_common_word():
    assert find_most_common_word("apple banana apple") == "apple"
    assert find_most_common_word("one two two three three three") == "three"
    assert find_most_common_word("") is None
    with pytest.raises("ValueError"):
        find_most_common_word(456)