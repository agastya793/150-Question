# Write a program to count the occurrences of a specific digit in a number.

def count_digit_occurences(num,digit):
    count = 0

    while num > 0:
        last_digit = num % 10
        if last_digit == digit:
            count += 1
        num = num // 10 
    return count  

number = int(input("enter a number: "))      
d = int(input("enter digit to count: "))

result = count_digit_occurences(number,d)
print("the digit",d,"appears",result,"times")