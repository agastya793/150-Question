# Write a program to find all Armstrong numbers within a given range.

start = int(input("enter start of range: "))
end = int(input("enter end of range: "))

print("Armstrong numbers are: ")

for num in range(start,end+1):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
       d = temp %10
       total += d** digits

       temp //= 10    

    if total == num:
        print(num)