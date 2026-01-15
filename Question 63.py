# Write a program to keep summing the digits of a number until a single digit is obtained.

def single_digit_sum(num):
    while num >= 10:
        total = 10

        while num > 0:
            digit = num % 10
            total += digit
            num = num // 10
        num =  total    
    return num

n = int(input("enter a number: "))   
print("single digit result: ", single_digit_sum(n)) 