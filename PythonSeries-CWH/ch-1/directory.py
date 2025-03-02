import os

# write here the path of the repo, for which you want all the files to get printed.
directory_path = './'

# Get a list of files and directories in the specified path
contents = os.listdir(directory_path)
print(contents)


