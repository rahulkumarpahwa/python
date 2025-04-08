num = int(input("Enter a number "))

prime = True
i = 2
while(i * i <= num):
    if(num % i == 0):
        prime = False
        break
    i+=1
    
if prime == True:
    print("The given number is prime")
else:
    print("The given Number is not prime")
