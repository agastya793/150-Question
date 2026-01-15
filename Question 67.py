# Write a program to find all divisors of a given number.

def find_divisor(num):
    divisors = []

    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)

    return divisors

n = int(input("enter a number: "))    
print("divisors of", n,"are", find_divisor(n))    
    