# Program: student_records.py
def process_student_records(students):
    """
    Processes a list of student dictionaries to return a dictionary
    of student names and their average marks (rounded to 2 decimal places).
    """
    averages = {}
    for student in students:
        name = student['name']
        marks = student['marks']
        average = sum(marks) / len(marks)
        averages[name] = round(average, 2)
    return averages

# Example Usage:
students = [
    {'name': 'Alice', 'marks': (80, 90, 85)},
    {'name': 'Bob', 'marks': (75, 85, 95)},
    {'name': 'Charlie', 'marks': (60, 70, 80)}
]
student_averages = process_student_records(students)
print(student_averages)
