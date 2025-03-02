# Program: utilities.py - Factorial Module
def factorial(num):
    """
    This function calculates the factorial of a number.
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
