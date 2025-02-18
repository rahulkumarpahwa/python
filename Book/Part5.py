#  Decision Control Instruction

# if-elif-else statement
if 5>3 : 
    print(5 , " is greater " , 3 )
elif 2>5:
    print(2 , " is greater " , 5 )
else :
    print("Both are equal")
    

# not() statement
print(not(1>-1))

a= int(input("Enter 0 or 1 "))
a = not a
print(a)

print("################################")
age = 19
if age < 18 : 
    status="minor"
else : 
    status = "adult"
print(status)