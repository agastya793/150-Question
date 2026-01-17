# Write a program to find the longest sequence of consecutive numbers in an array.

def longest_consecutive_sequence(arr):
    if not arr:
        return 0
    num_set = set(arr)
    longest = 0

    for num in num_set:
        #check if num is start of a sequence

        if num-1 not in num_set:
            current = num
            length = 1

            # count consecutive number
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest,length)    
        return longest
numbers = list(map(int,input("enter number: ").split())) 
print("length of longest consecutive sequence:", longest_consecutive_sequence(numbers))       