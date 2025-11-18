def count_words(text):
    word_count = 0
    if not isinstance(text, str):
        raise ValueError("not a string")
    elif text == "":
        return 0
    else:
        words = text.split()
        word_count = len(words)
    return word_count

def count_chars(text):
    if not isinstance(text, str):
        raise ValueError("not a string")
    elif text == "":
        return 0
    else:
        char_count = len(text)
        return char_count

def find_most_common_word(text):
    if not isinstance(text, str):
        raise ValueError("not a string")
    if text == "":
        return 0 
    words = text.split()
    
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    most_common_word = None
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_common_word = word

    return most_common_word

