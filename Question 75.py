# Write a program to generate multiplication tables for numbers within a specified range.

start = int(input("enter starting number: "))
end = int(input("enter ending number: "))

for num in range(start,end + 1):
    print(f"\nMultiplication Table of {num}")
    for i in range(1,11):
        print(f"{num}*{i} = {num * i}")