#ARU ABRAHAM
"""Program to find the roots of a quadratic equation(rounded to 2 decimal places)"""
from math import sqrt
a=float(input("Enter value of a "));
b=float(input("Enter value of b "));
c=float(input("Enter value of c"));
r = b**2 - 4*a*c
if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()
