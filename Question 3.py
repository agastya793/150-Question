 # Write a program to check if a given year is a leap year.

Year = int(input("Enter Year: "))

if ((Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0)):
    print("Leap Year")
else: 
    print("Not a Leap Year")