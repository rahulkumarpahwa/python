# Program: merge_dictionaries.py
def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries, summing values for common keys.
    """
    merged = dict1.copy()  # Start with a copy of dict1
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Add if key exists
        else:
            merged[key] = value   # Assign if key doesn't exist
    return merged

# Example Usage:
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)
