# Write a program to create different star patterns (e.g., pyramid, diamond).

''' 1.  *****
        *****
        *****
        *****
        ***** '''  

# SOLUTION :

'''| You see these pattern | Use this    |
| -------------------- | ----------- |
| Spaces go down       | `n - i`     |
| Spaces go up         | `i - 1`     |
| Stars go up          | `i`         |
| Stars go down        | `n - i + 1` |
| Centered pyramid     | `2*i - 1`   |'''

for i in range(5):
    for j in range(5):
        print("*" , end="")
    print()

