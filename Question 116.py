''' CCC
     BB
      A'''

n = 3
for i in range(n):
    print(" " * i,end="")

    # print characters
    print(chr(67-i) * (n-i))