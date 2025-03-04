# Lambda Functions with Filter
# Program to filter out odd numbers from a list ranging from 1 to 10

# List of numbers from 1 to 10
numbers = list(range(1, 11))

# Use filter to get only odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the odd numbers
print(odd_numbers)
