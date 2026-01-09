'''      *
        * *
       *   *
      *     *
     *********     '''


n = 5   

for i in range(1, n + 1):

    # print spaces before stars
    print(" " * (n - i), end="")

    # first row → only one star
    if i == 1:
        print("*")

    # last row → all stars
    elif i == n:
        print("*" * (2 * n - 1))

    # middle rows → two stars with spaces in between
    else:
        print("*" + " " * (2 * i - 3) + "*")

