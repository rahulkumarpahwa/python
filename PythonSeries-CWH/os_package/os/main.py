import os
# os.mkdir("apple") #this will create a folder apple

# similarly to create a range of folder:
for i in range(0, 100):
    if(not os.path.exists(f"apple/Day{i}")):
        os.mkdir(f"apple/Day{i}")
    
# on running once if we run again to create folder then it will give error.
# or you can check that using if condition as:
# if(not os.path.exists("apple")):
#     os.mkdir("apple") 
# this will first check that a folder name apple exists or not and then create the folder.


##########################################
# renaming in python
if(os.path.exists("apple.py")): 
    os.rename("apple.py", "mango.py") # source path, destination path

##########################################
# printing the list of folder in repo
folders = os.listdir("apple")
print(folders) # this will create a list of folders

for folder in folders:
    print(folder)
    
##############################################
# we can further go and print the files inside the folders

for folder in folders:
    print(os.listdir(f"apple/{folder}"))

# the above will print the file list, which contains the list of the files.


###############################
# to get the current directory name
print(os.getcwd())
# gives the path of the current folder

os.chdir("../") # makes you go one directory back and here we are changing the current directory

print(os.getcwd())


##################################
# we can learn about more methods ourself.

# like delete and more.