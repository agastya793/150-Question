# Write a program to create a matrix where elements form diagonal lines of a given pattern.
''' 1 0 0 0  
    1 1 0 0  
    1 1 1 0  
    1 1 1 1  '''

n = 4
for i in range(1,n+1):
    for j in range(1, n+1):
        if j <= i:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()        