#  Write a program to determine if a number is a perfect number.

num = int(input("enter a number: "))

total = 0

for i in range(1,num):
    if num % i == 0:
        total += i
if total == num:
    print(num, "is a perfect number")   
else:
    print(num, "is not a perfect number")         