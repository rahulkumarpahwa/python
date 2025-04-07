def welcome():
    print("You are welcome")
    
print(__name__)    
if __name__ == "__main__": #when called with the same then __name__ will main only then the welcome() method will be called, otherwise not.
    welcome()
    
# all the explanation is given in main.py 

# additional information:
# if we print the __name__ in and then compile the same file we will get the printed as "__main__"
# and when we call the main.py we get printed the "rahul" as the file name from where we import the function.
# basically name represents the place from where it is a called, when called within the same file its value is __main__. while when called from the other file its value is the name of the file from which we have imported.