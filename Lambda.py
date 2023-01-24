"""Lambda functions : Anonymus function or function without name:...
1.Filter 2.Map 3.Reduce.."""
from functools import reduce
# def square(a):
#     return a*a
f = lambda a,b:a*b
result=f(5,6)
#print(result)
"""Filters:...."""
# def is_even(n):
#     return n%2==0
num=[1,2,3,4,7,88,92,24]
even=list(filter(lambda n: n%2==0,num) )
print(even)
double=list(map(lambda n:n+n,even))
print(double)
sum=reduce(lambda a,b:a+b,double)
print(sum)