# Write a program to generate a pattern where each row contains the first few prime numbers.

# function to check prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+ 1):
        return False
    return True

n = int(input("enter number of rows: "))

primes = []
num = 2

# Grnerate required prime numbers
while len(primes) < n:
    if is_prime(num):
        primes.append(num)
    num += 1

# print pattern

for i in range(1,n+1) :
    for j in range(i):
        print(primes[j], end=" ")   
    print()        