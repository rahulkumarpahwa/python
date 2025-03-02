# Program: Lambda Function with Filter
numbers = range(1, 51)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
