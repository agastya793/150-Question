# Write a program to find the largest and smallest numbers in an array.

arr = list(map(int,input("enter numbers seperated by space : ").split()))

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("largest number:" , largest)  
print("smallest number:" , smallest)     