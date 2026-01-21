# solve quadratic equation

import math


a = float(input("enter value of a : "))
b = float(input("enter value of b: "))
c = float(input("enter value of c: "))

# calculate discriminant
d = b*b - 4*a*c

if d> 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("two real roots:", root1,"and", root2)

elif d == 0:
    root = -b/ (2*a)  
    print("one real root:" , root)
else:
    real = -b/(2*a)    
    imag = math.sqrt(-d) / (2*a)
    print("complex roots:")
    print(real,"+",imag,"i")
    print(real,"-",imag,"i")