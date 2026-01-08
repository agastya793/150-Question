# Write a program to check if a string or number is a palindrome.

value = input("Enter string or number: ")

# reverse input
rev = value[::-1]

if (value== rev):
    print("It is Palindrome")
else:
    print("It is not a Palindrome")