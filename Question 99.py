# Write a program to calculate the sum of the first N Fibonacci numbers.

n = int(input("enter value of n: "))

a = 0
b = 1
sum_fib = 0

for i in range(n):
    sum_fib += a
    c = a+ b
    a = b
    b = c

print("sum of first", n,"fibonacci numbers =", sum_fib)    