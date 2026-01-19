# Write a program to find common elements between two arrays.

arr1 = list(map(int,input("enter elements of first array: ").split()))
arr2 = list(map(int,input("enter elements of second array: ").split()))

common = []

for i in arr1:
    if i in arr2 and i not in common:
        common.append(i)
print("common elements:", common)        


'''another method

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

common = list(set(arr1) & set(arr2))
print("common elements:" , common)

'''