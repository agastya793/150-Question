'''         1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5    '''

n = 5

for i in range(1, n + 1):
    # spaces
    print("  " * (n - i), end="")

    # descending numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    # ascending numbers
    for j in range(2, i + 1):
        print(j, end=" ")

    print()
