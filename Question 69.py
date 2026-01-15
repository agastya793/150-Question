# Write a program to find the mode (most frequent number) in an array.

def find_mode(arr):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num,0)+ 1

    max_count = 0
    mode = None

    for num,count in frequency.items():
        if count > max_count:
            max_count = count
            mode = num

    return mode

numbers = [1,2,3,4,5,5,5,7,7,88,3,3,2] 
print("mode:", find_mode(numbers))       
    