'''    *        *
       **      **
       ***    ***
       ****  ****
       **********
       ****  ****
       ***    ***
       **      **
       *        *      '''


n = 5   # half height

# upper part
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# lower part
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)



