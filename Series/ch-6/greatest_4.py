a=input("enter the 1st number ")
b=input("enter the 2nd number ")
c=input("enter the 3rd number ")
d=input("enter the 4th number ")

if( int(a) > int(b) and int(a) > int (c) and int(a) > int(d) ):
    print(f"{a} is greatest. " )
elif(int(b)> int(c) and int(b) > int(d)):
    print(f"{b} is greatest. ")
elif(int(c)>int(d)):
    print(f"{c} is greatest. ")
else:
    print(f"{d} is greatest.")