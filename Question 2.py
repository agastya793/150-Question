# Write a program to determine if a number is prime.

num = int(input("Enter a number: "))
if (num <= 1 ):
    print("not a prime number")
else:
    for i in range (2,num):
        if(num % i== 0):
            print("not a prime number")
            break
        else:
            ("Prime Number")