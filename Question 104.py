# Write a program to count how many digits in a number are greater than a specific value.

num = int(input("enter a number: "))
value = int(input("enter comparison value: "))

count = 0

while num > 0:
    digit = num % 10
    if digit > value:
        count += 1
    num //= 10

print("count of digit greater than", value,"is:",count)        