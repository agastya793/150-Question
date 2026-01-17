# Write a program to find the sum of the digits of the product of two given numbers.

a = int(input("enter first number: "))
b = int(input("enter second number: "))

product = a*b
sum_digits = 0

temp = abs(product) # handle negative number

while temp > 0:
    sum_digits += temp % 10  #get last digit
    temp //= 10            # remove last digit
print("product =", product)    
print("sum of digits=", sum_digits)