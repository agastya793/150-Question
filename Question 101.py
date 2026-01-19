#  Write a program to count the number of words in a given string.

text = input("Enter a string: ")

# split string nto words

words = text.split()

# count words
count = len(words)

print("Number of words:", count)