#  Input 
a = input("Enter Your Name ")
print("Your Name is",a)

  
# case 1: 
num1 = input("enter num1: ")
num2 = input("enter num2: ")
print("sum of the two numbers is : ", num1+num2)
# sum of the two numbers is :  1234
# this is the output of the sum of the two numbers because the python takes the input in the form of the string always and when we try to add these, it got concatenated.
# so to add these we will have to typecast into integer.
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
print("sum of the two numbers is : ", num1+num2)
