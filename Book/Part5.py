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


################################
if -5>3:
   print("there is pass below")
elif 5> 3 : 
    pass
else : 
    print("There is pass above.")
    
    
print("################################################################")    

print("Practice Session")
qty = int(input("enter the quantity "))
price = float(input("Enter the price "))
dis = 10 if qty > 1000 else 0 
totalExpense = qty * price - qty * price * dis / 100
print("Total Expense = Rs." + str(totalExpense))

