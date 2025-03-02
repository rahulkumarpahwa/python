# 3. Find and Replace Words in a Large File Efficiently
def find_and_replace(input_file, output_file, old_word, new_word):
    """
    Reads a large text file line by line, replaces all occurrences of a specific word with another word,
    and writes the modified content to a new file. Uses readline() to optimize memory usage.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                modified_line = line.replace(old_word, new_word)
                outfile.write(modified_line)
        print(f"Successfully replaced '{old_word}' with '{new_word}' in '{input_file}' and wrote to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# find_and_replace('large_data.txt', 'modified_data.txt', 'AI', 'Artificial Intelligence')