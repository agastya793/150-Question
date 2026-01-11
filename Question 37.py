#  Write a program to count vowels and consonants in a given string.

text = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():          # check only letters
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
