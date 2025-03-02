# Commit: feat: Tuple duplicate checker and frequency counter
def tuple_duplicate_check():
    """
    Accepts a tuple of integers, checks for duplicates, and displays them with their frequencies.
    """
    try:
        input_str = input("Enter comma-separated integers: ")
        integer_tuple = tuple(map(int, input_str.split(',')))  # Convert input string to tuple of integers

        duplicates = {}
        for item in integer_tuple:
            if integer_tuple.count(item) > 1 and item not in duplicates:
                duplicates[item] = integer_tuple.count(item)

        if duplicates:
            print("Duplicate elements and their frequencies:")
            for item, frequency in duplicates.items():
                print(f"{item}: {frequency}")
        else:
            print("No duplicate elements found.")

    except ValueError:
        print("Invalid input. Please enter comma-separated integers only.")

# Run the function
tuple_duplicate_check()
