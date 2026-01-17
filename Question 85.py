# Write a program to extract and sum all numbers present in a given string.

def sum_of_numbers_in_string(s):
    total = 0
    current = ""

    for ch in s:
        if ch.isdigit():      # if character is a digit
            current += ch     # build number

        else:
            if current != ""  :
                total += int(current)  # add completed number
                current = ""   # reset for next number
     # if string end with a number
    if current != "" :   
        total += int(current)  
    return total

text = (input("enter a string: "))
print("sum of numbers in the string:", sum_of_numbers_in_string(text))

