# Write a program to calculate the sum of all prime numbers within a given range.

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num** 0.5)+ 1):
        if num % i == 0:
            return False
    return True

def sum_0f_prime(start,end):
    total = 0

    for n in range(start,end+ 1):
        if is_prime(n):
            total += n
    return total    

start = int(input("enter starting number: "))  
end = int(input("enter ending number: ")) 

print("sum of prime numbers:" , sum_0f_prime(start,end))