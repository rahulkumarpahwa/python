# Commit: feat: String processing: lowercase, filter length, and combine
def string_operations():
    """
    Accepts a string, splits it into words, converts to lowercase, filters words by length, and joins back into a string.
    """
    input_string = input("Enter a string of comma-separated words: ")
    words = input_string.split(',')
    processed_words = [word.lower() for word in words if len(word.strip()) >= 4]  #strip to remove leading/trailing spaces

    result_string = ','.join(processed_words)
    print(result_string)

# Run the function
string_operations()
