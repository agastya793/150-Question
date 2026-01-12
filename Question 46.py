# Write a program to find the sum of all even numbers within a given range.


start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

total = 0

for i in range(start, end+1):
    if i % 2 == 0:
        total += i
print("sum of even numbers =" , total)        
        