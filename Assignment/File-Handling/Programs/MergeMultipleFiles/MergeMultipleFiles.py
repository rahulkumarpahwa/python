# 2. Merging Multiple Files into One

def merge_files(input_files, output_file):
    """
    Takes multiple text files as input and merges their content into a single output file.
    Ensures that each file's content starts on a new line in the merged file.
    """
    try:
        with open(output_file, 'w') as outfile:
            for file_name in input_files:
                try:
                    with open(file_name, 'r') as infile:
                        content = infile.read()
                        outfile.write(content + '\n')  # Add content and a newline
                except FileNotFoundError:
                    print(f"Error: File '{file_name}' not found.")
                except Exception as e:
                    print(f"An error occurred while reading '{file_name}': {e}")
        print(f"Successfully merged files into '{output_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# merge_files(['file1.txt', 'file2.txt', 'file3.txt'], 'merged_output.txt')
