#  for now we creating a new file from the old file to get the new file with new name. but we can OS module to delete the file as well.

with open("old.txt", "r") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)