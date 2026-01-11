# Write a program to compute the factorial of a given number.


num = int(input("enter a number : "))

factorial = 1

if num < 0:
   print("factorial is not defined for negative numbers.")
else:
   for i in range(1,num+1):
      factorial *= i
print("factorial of" , num, "is",factorial)