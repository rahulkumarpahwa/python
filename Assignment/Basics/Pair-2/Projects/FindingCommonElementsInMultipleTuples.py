# 5. Finding Common Elements in Multiple Tuples
def find_common_elements(tuple1, tuple2, tuple3):
    """
    Takes three tuples as input and returns a new tuple containing elements that are common in all three.
    """
    set1 = set(tuple1)
    set2 = set(tuple2)
    set3 = set(tuple3)

    common_elements = set1.intersection(set2, set3)
    return tuple(common_elements)

# Example Usage:
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (4, 5, 6, 7)
common = find_common_elements(tuple1, tuple2, tuple3)
print(common)  # Output: (4,)