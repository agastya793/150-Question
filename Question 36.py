# Write a program to find the LCM of two numbers.

a = int(input("enter first number: "))
b = int(input("enter second number: "))

# find GCD
x,y = a,b
while y != 0:
    x,y = y, x% y

gcd = x
# formula for lcm

lcm = (a*b) // gcd

print("lcm is :" , lcm)
