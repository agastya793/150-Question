# Write a program to count the frequency of each character in a given string.

text = input("enter a string: ")
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1

    else:
        freq[char]  = 1
print("character frequency:")          
for key, value in freq.items():
    print(key,":" , value)