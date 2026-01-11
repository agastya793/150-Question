# Write a program to calculate the sum of digits of a number.

num = input("enter a number : ")
total = 0
for digit in num:
    total += int(digit)
print("sum of digit:" , total)