# Install the NumPy module using pip (provide the command for installation).
# pip install numpy

# Program: NumPy Matrix Transpose
import numpy as np

# Generate a 2x3 matrix with random numbers between 0 and 10
matrix = np.random.randint(0, 11, size=(2, 3))
print("Original Matrix:")
print(matrix)

# Compute the transpose of the matrix
transpose = matrix.T
print("\nTranspose of the Matrix:")
print(transpose)
