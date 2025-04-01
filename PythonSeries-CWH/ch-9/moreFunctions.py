f = open("./file2.txt")
lines = f.readlines()
print(lines)
print(type(lines))
f.close()  # must close

# output:
# ['this is a random text to be generated and to be learned/ read from a function.\n', 'this is second line.\n', 'this is third line to be read by the function readlines.']

# also the type is : <class 'list'>

f= open("./file2.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)


line3 = f.readline()
print(line3)


line4 = f.readline()
print(line4 == "") # s no fourth line, it will return True
f.close()


# so basically their two types of function in python 
# 1. readlines(), which can read multipe lines and put them in a list.
# 2. readline(), which read only one line a time and on further calling read the next lines. (without opening again or closing)
# Also after the all lines are read and if we call the further readline it will print nothing or empty string.

# we can make the use of WHILE as :
print("-------------------------------------------------")

f = open("./file2.txt", "r")
line = f.readline()
while(line != ""):
    print(line)
    line  = f.readline()
f.close()