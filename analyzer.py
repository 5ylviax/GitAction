def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    char_count = len(text)
    return char_count

def find_most_common_word(text):
    words = text.split()
    if not words:
        return None
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


# print(count_words("hello"))
# print(count_chars("hello"))
# print(find_most_common_word("one two three three three"))
