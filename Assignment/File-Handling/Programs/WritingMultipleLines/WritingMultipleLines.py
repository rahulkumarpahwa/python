# 5. Writing Multiple Lines to a File
def write_multiple_lines(output_file):
    """
    Asks the user to enter lines until they type "STOP" and writes them to a file.
    Uses writelines() to write all the lines at once.
    """
    lines = []
    print("Enter text (type 'STOP' to finish):")
    while True:
        line = input()
        if line.upper() == "STOP":
            break
        lines.append(line + '\n')  # Add a newline character to each line

    try:
        with open(output_file, 'w') as file:
            file.writelines(lines)
        print(f"Contents written to '{output_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# write_multiple_lines('output.txt')