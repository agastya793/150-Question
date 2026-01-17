# Write a program to find how many perfect numbers exist up to a given limit.

def is_perfect(num):
    if num <=1:
        return False
    
    total = 1

    for i in range(2,int(num**0.5)+ 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total == num


def count_perfect_numbers(limit):
    count = 0 

    for num in range(2,limit + 1):
        if is_perfect(num):
            count += 1
    return count   

n = int(input("enter the limit: "))    
print("number of perfect numbers up to",n,":", count_perfect_numbers(n)) 
