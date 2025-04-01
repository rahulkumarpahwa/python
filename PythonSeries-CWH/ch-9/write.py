#  here we are writing in a file.
string = "This is a string to be written"
f = open("./newFile.txt", "w") 
f.write(string)
f.close()

# note : 
# 1. if file does nt exist it will create the file.
# 2. to write, open the file in write mode.