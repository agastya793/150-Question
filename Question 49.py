# Write a program to print all prime numbers less than a given number.

n = int(input("enter a number: "))
print("prime number less than" , n, "are:")

for num in range(2,n):
    is_prime = True

    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  
            break
    if is_prime:
        print(num, end=" ")    