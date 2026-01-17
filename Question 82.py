# Write a program to find the largest prime factor of a given number.

def largest_prime_factor(n):
    largest = -1

    # Remove all factors of 2
    while n % 2 == 0:
        largest = 2
        n //= 2

    # Check odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2

    # If n is still greater than 2, it is prime
    if n > 2:
        largest = n

    return largest


# Input
num = int(input("Enter a number: "))
print("Largest prime factor:", largest_prime_factor(num))
