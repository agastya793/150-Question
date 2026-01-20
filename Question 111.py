# Write a program to find the length of the longest word in a given string.

text =input("enter a string: ")
words = text.split()
longest_length = 0

for word in words:
    if len(word) > longest_length:
        longest_length = len(word)
print("length of the longest word:" , longest_length)        