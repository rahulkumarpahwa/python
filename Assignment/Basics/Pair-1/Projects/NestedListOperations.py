# Commit: feat: Nested list manipulation: min/max, even replacement
def nested_list_operations():
    """
    Creates a nested list, finds min/max in each sublist, replaces even numbers, and prints the updated list.
    """

    nested_list = []
    while True:
        try:
            input_str = input("Enter comma-separated integers for a sublist (or type 'done'): ")
            if input_str.lower() == 'done':
                break
            sublist = list(map(int, input_str.split(',')))
            nested_list.append(sublist)
        except ValueError:
            print("Invalid input. Please enter comma-separated integers only.")

    if not nested_list:
        print("No sublists were entered.")
        return

    for sublist in nested_list:
        if sublist:  # Make sure the sublist is not empty
            print(f"Original sublist: {sublist}")
            print(f"Maximum value: {max(sublist)}")
            print(f"Minimum value: {min(sublist)}")

            for i in range(len(sublist)):
                if sublist[i] % 2 == 0:
                    sublist[i] = "Even"
            print(f"Modified sublist: {sublist}")
        else:
            print("Empty sublist found.")

# Run the function
nested_list_operations()
