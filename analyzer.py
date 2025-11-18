def count_words(self, text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(self, text):
    char_count = len(text)
    return char_count

def find_most_common_word(self, text):
    from collections import Counter
    words = text.split()
    if not words:
        return None
    word_counts = Counter(words)
    common, _ = word_counts.most_common(1)[0]
    return common