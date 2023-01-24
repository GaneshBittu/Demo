n=int(input("enter a number:"))
#prime number is always greater than 1
if n >1:
    for i in range(2,n):
        if n%i == 0:
            print(n,"not a prime number")
            break
    else:
        print(n,"Is a prime number")
#Entered number is less than or equal to 1
#then it is not a prime number"""
else:
    print(n," is not a prime")