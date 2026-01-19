# Write a program to calculate the sum of the first N even numbers.

n = int(input("enter a number: "))
sum_even = 0
for i in range(1,n+1):
    sum_even += 2 * i
print("sum of first" , n,"even numbers=",sum_even)    

'''another method

n = int(input("Enter N: "))
print("Sum =", n * (n + 1))




'''