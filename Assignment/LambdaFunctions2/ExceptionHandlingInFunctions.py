# Exception Handling in Functions
# Function to divide two numbers with exception handling

def divide_numbers(a, b):
    try:
        # Attempt to divide the numbers
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result

# Test cases
results = [
    divide_numbers(10, 2),  # Valid division
    divide_numbers(10, 0),  # Division by zero
    divide_numbers(10, 'a')  # Non-numeric input
]

# Print the results
print(results)
