# Write a program to find the median value of a list of numbers.

nums = list(map(int,input("enter numbers: ").split()))

nums.sort()

n = len(nums)
if n  % 2 == 1:
    median = nums[n // 2]
else:
    median = (nums[n // 2-1] + nums[n // 2]) / 2
print("median =" , median)       