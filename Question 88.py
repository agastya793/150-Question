# Write a program to check which numbers in a given range are perfect squares.

start = int(input("enter starting number: "))
end = int(input("enter ending number: "))

i =1
print("perfect squares in the range are: ")

while i * i <= end:
    square = i* i
    if square >= start:
        print(square)
    i += 1
        
