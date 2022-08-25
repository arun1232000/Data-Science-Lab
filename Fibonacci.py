#ARUN ABRAHAM
#Program to print the first N Fibonacci numbers.
n=int(input("enter a limit"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    s=a+b
    print(s)
    a=b
    b=s
