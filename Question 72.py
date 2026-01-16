#  Write a program to find the second largest number in an array.

def second_largest(arr):
    if len(arr) < 2:
        return None 
    
    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second 

numbers = [10,5,20,8]    
print("second largest number:",second_largest(numbers))       