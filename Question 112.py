# Write a program to calculate the difference between the sum of even and odd numbers in an array.

arr = list(map(int,input("enter elements of array: ").split()))
even_sum = 0
odd_sum = 0

for num  in arr:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num    
difference = even_sum - odd_sum        

print("sum of even numbers: ", even_sum)
print("sum of odd numbers:",odd_sum)
print("difference :", difference)