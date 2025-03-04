# Custom Module Creation and Importing
# Creating a module named utilities.py for factorial calculation

# Step 1: Create the module utilities.py
module_code = """\ndef factorial(num):\n    \"\"\"Function to calculate factorial of a number\"\"\"\n    if num == 0 or num == 1:\n        return 1\n    else:\n        return num * factorial(num - 1)\n"""

# Write the module to a file
with open("utilities.py", "w") as file:
    file.write(module_code)

# Step 2: Write a script to import and use the module
import utilities

# Calculate factorial for numbers 1 to 10
factorials = [utilities.factorial(i) for i in range(1, 11)]

# Print the factorials
print(factorials)
