# Write a program to find the Fibonacci number at a specific position.
n = int(input("enter position: "))

if n <= 0:
    print("enter a positive number")
elif n == 1:
    print("fibonaci number at position 1 is 0")  
elif n ==2:
    print("fibonacci number at position 2 is 1") 
else:
    a = 0
    b = 1
    for i in range(3,n+ 1):
        c = a + b
        a = b
        b = c     
    print("fibonacci number at position",n,"is", b)        