# PACKAGE CREATION:
# main.py
#Demonstrates how to import and use functions from the my_package package

import sys
sys.path.append('./my_package')  # Add the package directory to the Python path

from my_package import data_handler, utilities

# Use the functions from the package
file_content = data_handler.read_data('input.txt')
print(f"Content from file: {file_content}")

utility_message = utilities.utility_function()
print(utility_message)
