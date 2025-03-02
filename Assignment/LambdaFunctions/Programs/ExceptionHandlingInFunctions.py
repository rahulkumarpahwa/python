# Program: Exception Handling
def divide(x, y):
    """
    This function divides two numbers and handles potential exceptions.
    """
    try:
        result = x / y
        print(f"{x} / {y} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage:
divide(10, 2)
divide(10, 0)
divide(10, "a")
