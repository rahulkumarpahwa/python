a= int(input("enter the marks of 1st subject. "))
b= int(input("enter the marks of 2nd subject. "))
c= int(input("enter the marks of 3rd subject. "))
total = a+b+c
total_percent = (total/ 300 ) 


if ( total_percent >= 0.4 and a/100 >= 0.33 and b/100 >= 0.33 and c/100 >= 0.33 ):
    print("The Student Pass the exam")
else:
    print("The Student has failed.") 