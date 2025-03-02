# SQLITE DATABASE OPERATIONS:
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        grade TEXT
    )
''')

# Insert data into the table
students_data = [
    (1, 'Alice', 'A'),
    (2, 'Bob', 'B'),
    (3, 'Charlie', 'C'),
    (4, 'David', 'B'),
    (5, 'Eve', 'A+')
]

cursor.executemany('INSERT INTO students (id, name, grade) VALUES (?, ?, ?)', students_data)

# Retrieve all records from the table
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Display the records
for row in rows:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
