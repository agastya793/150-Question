# Write a program to find the GCD of two numbers.

a = int(input("enter first number : "))
b = int(input("enter second number : "))

while b!=0:
    a,b=b,a%b
print("GCD is :", a)  
