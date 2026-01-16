# Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.

n = int(input("enter a number: "))
total = 0.0
for i in range(1,n+1):
    total += 1/i

print("sum of the series:" , total)    