# Lambda Functions & Map
# Program to square numbers from 1 to 20 using lambda and map

# List of numbers from 1 to 20
numbers = list(range(1, 21))

# Lambda function to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

# Print the squared numbers
print(squared_numbers)
