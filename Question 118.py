'''     A
       BCD
      EFGHI   '''

rows = 3
ch = 65 # ASII value of A

for i in range(1,rows+1):
    # print spaces
    print(" " * (rows - i), end="")

    # print characters

    for j in range(2* i-1):
        print(chr(ch), end="")
        ch += 1
    print()    