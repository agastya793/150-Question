#  Write a program to reverse a given string.

text = input("enter a string: ")

rev = ""
for ch in text:
    rev = ch + rev

print("Reversed string:" , rev)    

# another method
''' text = input("Enter a string: ")
    print("Reversed string:", text[::-1])
'''