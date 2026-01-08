''' *****
    ****
    ***
    **
    *      '''




'''| You see these pattern | Use this    |
| -------------------- | ----------- |
| Spaces go down       | `n - i`     |
| Spaces go up         | `i - 1`     |
| Stars go up          | `i`         |
| Stars go down        | `n - i + 1` |
| Centered pyramid     | `2*i - 1`   |'''


for i in range(1,6):
    for j in range(5-i+1):
        print("*",end="")
    print()