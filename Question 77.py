# Write a program to count how many palindromic substrings exist in a given string.

def count_palindromic_substrings(s):
    count = 0
    n = len(s)

    # Function to expand around center
    def expand(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    # Try every possible center
    for i in range(n):
        expand(i, i)       # odd length palindromes
        expand(i, i + 1)   # even length palindromes

    return count


# Input
text = input("Enter a string: ")
print("Number of palindromic substrings:", count_palindromic_substrings(text))

