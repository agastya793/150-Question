# Write a program to find the sum of the digits of the factorial of a given number.

n = int(input("enter a number: "))

# find factorial
fact = 1
for i in range(1, n+1):
    fact *= i

# sum of digits of factorial
sum_digits = 0
temp = fact

while  temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("factorial of" , n , "is" , fact)  
print("sum of digits of factorial is:" , sum_digits)  