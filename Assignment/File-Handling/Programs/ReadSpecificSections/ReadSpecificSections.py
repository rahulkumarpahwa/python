# 4. Read Specific Sections from a Large File Using seek() and tell()
def extract_text_section(input_file, start_position, end_position):
    """Reads a large text file and extracts text between specified start and end positions using seek() and tell()."""
    try:
        with open(input_file, 'r') as file:
            file.seek(start_position)
            extracted_content = file.read(end_position - start_position)
            return extracted_content
    except FileNotFoundError:
        return f"Error: File '{input_file}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
# extracted_text = extract_text_section('large_data.txt', 10, 50)
# print(extracted_text)