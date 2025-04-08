# factorial 
num = int(input("Enter a Number "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    
print(f"the factorial of a number is {fact}")