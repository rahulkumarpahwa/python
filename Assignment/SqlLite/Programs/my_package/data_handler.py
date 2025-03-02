# my_package/data_handler.py
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
