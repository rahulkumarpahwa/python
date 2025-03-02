# 3. Sort List of Tuples
def sort_student_tuples(student_list):
    """
    Sorts a list of tuples (name, marks) based on marks in descending order.
    If marks are the same, sorts alphabetically by name.
    """
    return sorted(student_list, key=lambda x: (-x[1], x[0]))

# Example Usage:
student_list = [("Alice", 85), ("Bob", 95), ("Charlie", 85), ("Dave", 90)]
sorted_list = sort_student_tuples(student_list)
print(sorted_list) # Output: [('Bob', 95), ('Dave', 90), ('Alice', 85), ('Charlie', 85)]