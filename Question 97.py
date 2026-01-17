# Write a program to find all divisors of the product of two given numbers.

a = int(input("enter first number: "))
b = int(input("enter second number: "))

product = a*b

print("product = " , product)
print("Divisor of the product are: ")


for i in range(1,product +1):
    if product % i == 0:
        print(i,end=" ")