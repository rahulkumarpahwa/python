# 2. Find Duplicate Elements Efficiently
def find_duplicates(input_list):
    """
    Finds and returns all duplicate elements from a list of numbers in O(n) time complexity.
    """
    seen = set()
    duplicates = set()

    for num in input_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example Usage:
input_list = [1, 2, 3, 4, 2, 5, 6, 3]
duplicate_list = find_duplicates(input_list)
print(duplicate_list)  # Output: [2, 3]