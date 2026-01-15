#  Write a program to determine if a number is a perfect square.

def is_perfect_square(num):
    if num < 0:
        return False
    
    i = 0
    while i * i <= num:
        if i* i == num:
            return True
        i += 1
    return False

n = int(input("enter a number: ")) 

if is_perfect_square(n):
    print(n,"is a perfect square")
else:
    print(n,"is not a perfect square")    