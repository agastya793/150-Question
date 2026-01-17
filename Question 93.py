# Write a program to check for palindromic numbers within a given range.

start = int(input("enter a start of range: "))
end = int(input("enter end of range: "))

print("palindrome number in range are:")

for num in range(start,end+1):
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    if num == reverse:
        print(num,end=" ")    