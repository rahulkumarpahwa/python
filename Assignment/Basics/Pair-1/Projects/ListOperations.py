# Commit: feat: List operations: remove duplicates, find second largest, sort
def list_operations():
    """
    Accepts a list of integers, removes duplicates, finds the second largest element, and sorts the list.
    """
    try:
        input_str = input("Enter comma-separated integers: ")
        num_list = list(map(int, input_str.split(',')))

        # Remove duplicates
        unique_list = list(dict.fromkeys(num_list))  # preserves order while removing duplicates

        # Find second largest
        if len(unique_list) >= 2:
            sorted_list = sorted(unique_list, reverse=True)
            second_largest = sorted_list[1]
            print(f"Second largest element: {second_largest}")
        else:
            print("List does not contain enough elements to find the second largest.")

        # Sort the modified list
        unique_list.sort()
        print(f"Sorted unique list: {unique_list}")

    except ValueError:
        print("Invalid input. Please enter comma-separated integers only.")

# Run the function
list_operations()
