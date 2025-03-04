# Using External Modules
# Install and use the NumPy module to sum random numbers between 0 and 10

# Import necessary libraries
import numpy as np

# Generate 10 random numbers between 0 and 10
random_numbers = np.random.uniform(0, 10, 10)

# Calculate the sum of the random numbers
sum_random_numbers = np.sum(random_numbers)

# Print the random numbers and their sum
print("Random Numbers:", random_numbers)
print("Sum of Random Numbers:", sum_random_numbers)
