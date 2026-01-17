# Write a program to calculate the sum of the first N prime numbers.

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_first_n_primes(n):
    count = 0
    num = 2
    total = 0

    while count < n:
        if is_prime(num):
            total += num
            count += 1
        num += 1
    return total

n = int(input("enter number: "))      
print("sum of first", n , "prime numbers: ", sum_of_first_n_primes(n))  
