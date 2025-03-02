# Program: dictionary_sort.py
def sort_dictionary_lists(data):
    """
    Sorts each list within a dictionary in descending order.
    """
    for key, value in data.items():
        data[key] = sorted(value, reverse=True)
    return data

# Example Usage:
data = {
    "A": [3, 1, 4, 1, 5],
    "B": [10, 2, 8, 6],
    "C": [7, 3, 1, 9]
}
sorted_data = sort_dictionary_lists(data)
print(sorted_data)
