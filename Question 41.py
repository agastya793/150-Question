# Write a program to find the sum of elements in an array.

arr = list(map(int,input("enter number seperated by space: ").split()))

total = 0
for num in arr:
    total += num
print("sum of elements in array:" , total)    