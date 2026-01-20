''' 0101
    1010
    0101
    1010'''

n = 4

for i in range(n):
    for j in range(n):
        print((i+ j) % 2, end="")
    print()    

    #   If row + column is even → print 0
    #   If row + column is odd → print 1