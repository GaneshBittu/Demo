n=1221
temp=n
rev=0
while n > 0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp ==rev:
    print("is palindome :")
else:
    print("is not a palindrome")