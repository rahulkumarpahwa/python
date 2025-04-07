import rahul
rahul.welcome()

# now here "You are welcome" will be print twice because one time we are importing the rahul.py and in rahul.py we have already called the method welcome and next time is due to our call we made here again to welcome.

# to solve this problem we will go to rahul.py and write the if statement as: 
# if __name__ == "__main__":
#     welcome()

# this will make the call to welcome only when the file main.py will call it here and also when we directly compile the rahul.py and not twice anymore.