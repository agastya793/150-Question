# Write a program to find the second smallest number in an array.

arr = list(map(int,input("enter the number: ").split()))
unique = list(set(arr))
unique.sort()

if len(unique) < 2:
    print("no second smallest elements")
else:
    print("second smallest number is: " , unique[1])    