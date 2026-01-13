#  Write a program to calculate the power of a number.

def power(base,exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


b = int(input("enter base: "))
e = int(input("enter exponent: "))

print("Result:", power(b,e))