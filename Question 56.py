# Write a program to find the median of an array of numbers.

def find_median(arr):
    arr.sort()
    n = len(arr)

    mid = n// 2

    if n% 2 != 0:
        return arr[mid]
    else:
        return (arr[mid-1]+ arr[mid])/ 2
    
numbers = [7,2,5,1,9,19]
print("median:",find_median(numbers))