f = open("./file.txt") 
data = f.read()
print(data)
f.close()

# by-default mode is read "r", which we pass along with the open as argument but we can open the file in the other mode as well as:
# f = open("./file.txt", "w")


 