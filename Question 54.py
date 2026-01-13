# Write a program to find the largest palindrome in a given string.

s = input("Enter a string: ")

longest = ""

n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        sub = s[i:j]
        if sub == sub[::-1]:      # checks if substring is palindrome
            if len(sub) > len(longest):
                longest = sub

if longest != "":
    print("Largest palindrome is:", longest)
else:
    print("No palindrome found")
