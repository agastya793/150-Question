# Write a program to find missing numbers in a sequence from 1 to n.

def find_missing_numbers(arr , n):
    expected = set(range(1, n+ 1))
    actual = set(arr)

    missing = expected - actual
    return sorted(missing)

nums = [1,2,3,4,6,7]
n= 8

print("missing numbers:" , find_missing_numbers(nums,n))