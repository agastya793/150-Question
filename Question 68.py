# Write a program to calculate the average of numbers in an array.

def calculate_average(arr):
    total = 0

    for num in arr:
        total += num
    average = total / len(arr)    
    return average

numbers = [10,3,90,69,65,78]
print("average : ", calculate_average(numbers))