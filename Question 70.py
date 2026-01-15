# Write a program to determine the length of a string without using built-in functions.

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


# Input
text = input("Enter a string: ")
print("Length of the string:", string_length(text))
