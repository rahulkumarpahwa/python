# Commit: feat: Sentence Reversal with Capitalization
def reverse_sentence():
    """
    Accepts a sentence, reverses the order of words, and ensures each word is capitalized.
    """
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_words = words[::-1]
    capitalized_words = [word.capitalize() for word in reversed_words]
    result = " ".join(capitalized_words)
    print(result)

# Run the function
reverse_sentence()
