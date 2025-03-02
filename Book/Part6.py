# 
for key in {'A101' : 'Rajesh', 'A111' : 'Sunil', 'A112' : 'Rakesh'} :
 print(key)
 
lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose'] 
for i, ele in enumerate(lst) :
 print(i, ele)
 
 
# check if the number is prime or not.
num=int(input("Enter a number"))
i = 2
prime = True
while i * i <= num :
    if num % i == 0:
        prime= False
    i+=1

if prime : 
    print("Prime Number")
else :
    print("Not prime")
    
    
for ele in [10, 20, 30, 3, 40, 50] :
 if ele % 10 != 0 : 
    print(ele, 'is a not a multiple of 10')
    break
 else : 
    print('all numbers in list are multiples of 10')
