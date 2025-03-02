# 1. Reverse File Content Using File Pointer Manipulation

def reverse_file_content(input_file, reversed_file):
    """
    Reads a text file, reverses its content, and writes it to a new file.
    Also, displays the last 10 characters from the reversed file.
    """
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        reversed_content = content[::-1]

        with open(reversed_file, 'w') as file:
            file.write(reversed_content)

        with open(reversed_file, 'r') as file:
            file.seek(0, 2)  # Go to the end of the file
            file_size = file.tell()
            start_position = max(file_size - 10, 0)  # Ensure start position is not negative
            file.seek(start_position, 0)  # Go to the start position
            last_chars = file.read()
        
        print(f"Last 10 characters of reversed file: {last_chars}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# reverse_file_content('input.txt', 'reversed_output.txt')