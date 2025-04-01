# to remove the headache of closing the file we use the with.py

f = open("file.txt")
print(f.read())
f.close()

print("-------------------------------------------")
#  above can be written as :

with open("file.txt") as f :
    print(f.read())
    
#  so here we use the WITH keyword due to which we don't need to write the f.close()