# Write a program to check if a number is a narcissistic number

'''A number is narcissistic if:

Sum of each digit raised to the power of total digits
=
Original number

a narcissistic number is the same as an Armstrong number 
'''

num = int(input("enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10 
if sum == num:
    print(num, "is a narcissistic number")
else:
    print(num,"is not a narcissistic number")    


