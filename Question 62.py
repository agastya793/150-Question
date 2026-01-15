# Write a program to find the sum of the squares of the digits of a number.

def sum_of_squares_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit * digit
        num = num // 10

    return total

n = int(input("enter a number: "))
print("sum of squares of digits:" , sum_of_squares_of_digits(n))    