# 1. List Transformation Function
def transform_list(input_list):
    """
    Takes a list of integers, doubles even-indexed elements,
    halves odd-indexed elements, and reverses the list.
    """
    transformed_list = []
    for i, num in enumerate(input_list):
        if i % 2 == 0:  # Even index
            transformed_list.append(num * 2.0)
        else:  # Odd index
            transformed_list.append(num / 2.0)
    
    transformed_list.reverse()
    return transformed_list

# Example Usage:
input_list = [10, 20, 30, 40, 50]
output_list = transform_list(input_list)
print(output_list)  # Output: [25.0, 20.0, 15.0, 20.0, 5.0]