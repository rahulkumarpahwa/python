# Program: most_frequent_word.py
import re
from collections import Counter

def most_frequent_word(text):
    """
    Finds the most frequent word(s) in a text, ignoring case.
    Returns a list if multiple words have the same frequency.
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counts = Counter(words)
    max_count = max(word_counts.values())
    most_frequent = [word for word, count in word_counts.items() if count == max_count]
    return most_frequent

# Example Usage:
text = "The Python language is great. Python is easy to learn. Learn Python"
result = most_frequent_word(text)
print(result)
