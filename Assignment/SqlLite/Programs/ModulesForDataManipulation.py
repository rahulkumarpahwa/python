# data_handler.py
# MODULES FOR DATA MANIPULATION:

def read_data(file_path):
    """Reads a text file and returns its content."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_data(data, file_path):
    """Writes data to a text file."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Data written successfully."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    # Demonstrate reading and writing
    file_to_read = 'input.txt'
    file_to_write = 'output.txt'

    # Create a sample input file
    with open(file_to_read, 'w') as f:
        f.write("This is a sample text in input.txt")

    # Read data from the input file
    content = read_data(file_to_read)
    print(f"Content read from {file_to_read}:\n{content}")

    # Write the content to another file
    write_result = write_data(content, file_to_write)
    print(write_result)

    # Verify the content of the output file
    read_output = read_data(file_to_write)
    print(f"Content of {file_to_write}:\n{read_output}")
