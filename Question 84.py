# Write a program to check if a given string with brackets is balanced

def is_balanced(s):
    prev_length = -1

    # keep removing valid pairs until no change occur
    while prev_length != len(s):
        prev_length = len(s)
        s = s.replace("()" , "")
        s = s.replace("[]", "")
        s = s.replace("{}","")

        # if string become empty, it's balanced
        return s == ""
    
    text = input("enter a string with brackets: ")

    if is_balanced(text):
        print("the string is balanced.")
    else:
        print("string is not balanced")    