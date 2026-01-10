'''      1
        212
       32123
      4321234
       32123
        212
         1    '''



n = 4   # height of the top half

# upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i, 0, -1):     # decreasing numbers
        print(j, end="")

    for j in range(2, i + 1):    # increasing numbers
        print(j, end="")

    print()

# lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(i, 0, -1):
        print(j, end="")

    for j in range(2, i + 1):
        print(j, end="")

    print()
