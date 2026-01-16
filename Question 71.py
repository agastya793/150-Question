# Write a program to find the sum of the prime factors of a given number.

def  sum_of_prime_factors(num):
    total = 0
    factor = 2


    while num > 1:
        while num % factor == 0:
            total += factor
            num = num // factor
        factor +=1

    return total       

n = int(input("enter a number: "))
print("sum of prime numbers: ", sum_of_prime_factors(n))