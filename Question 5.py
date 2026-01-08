# Write a program to generate the Fibonacci series up to a given number.
num = int(input("Enter Number: "))
a = 0
b = 1

print("Fibonacci Series: ")
while(a<= num):
    print(a,end = " ")
    c = a+b
    a = b
    b = c