# DATABASE AND EXCEPTION HANDLING:
import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Attempt to create the table (if it doesn't exist)
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                grade TEXT
            )
        ''')
        print("Table created successfully (if it didn't exist).")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

    # Attempt to insert data
    try:
        students_data = [
            (1, 'Alice', 'A'),
            (2, 'Bob', 'B'),
            (3, 'Charlie', 'C'),
            (4, 'David', 'B'),
            (5, 'Eve', 'A+')
        ]
        cursor.executemany('INSERT INTO students (id, name, grade) VALUES (?, ?, ?)', students_data)
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

    # Attempt to retrieve data
    try:
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error retrieving data: {e}")

    # Commit changes
    try:
        conn.commit()
        print("Changes committed successfully.")
    except sqlite3.Error as e:
        print(f"Error committing changes: {e}")

except sqlite3.Error as e:
    print(f"Connection error: {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
