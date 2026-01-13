# Write a program to find the N-th triangular number.

'''A triangular number is the sum of the first N natural numbers.
'''

def triangular_number(n):
    return n*(n+1)// 2

n = int(input("enter n: "))
print("the",n,"th triangular number is:",triangular_number(n))