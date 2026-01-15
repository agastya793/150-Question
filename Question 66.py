# Write a recursive program to generate the Fibonacci sequence up to a given number.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("enter number of terms: "))

print("fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")