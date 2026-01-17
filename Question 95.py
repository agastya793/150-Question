# Write a program to count how many times a specific word appears in a given string

text = input("Enter a sentence: ")
word = input("Enter the word to count: ")

count = text.split().count(word)

print("The word appears", count, "times.")
