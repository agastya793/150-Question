# Write a program to calculate the sum of squares of all even numbers up to a given N.

n = int(input('enter a number: '))

sum_squares = 0

for i in range(2, n+1,2):
    sum_squares += i *i

print("sum of squares of even numbers: " , sum_squares)    