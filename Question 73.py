#  Write a program to find the longest substring without repeating characters in a given string.

def longest_unique_substring(s):
    longest = ""

    for i in  range(len(s)):
        current = ""

        for j in range(i,len(s)):
            if s[j] in current:
                break
            current +=s[j]
        if len(current) > len(longest) :
            longest = current
    return longest

text = input("enter a string: ")  
print("longest substring:" , longest_unique_substring(text))        
