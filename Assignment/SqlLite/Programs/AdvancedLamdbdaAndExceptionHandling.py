# ADVANCED LAMBDA AND EXCEPTION HANDLING:
# Lambda and Exception Handling

def inverse(x):
    """
    Returns the inverse of a number using a lambda function.
    Handles exceptions for zero and non-numeric inputs.
    """
    try:
        # Define a lambda function to calculate the inverse
        inverse_func = lambda a: 1 / float(a)

        return inverse_func(x)
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except (TypeError, ValueError):
        return "Invalid input: Must be a number!"

# Test the lambda function with a list of values
test_values = [2, 0, 'hello', 5.5, -10, [1,2]]

for value in test_values:
    result = inverse(value)
    print(f"The inverse of {value} is: {result}")
