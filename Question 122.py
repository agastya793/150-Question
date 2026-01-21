# addition of two matrix

A = [[1,4,7],
     [6,8,9],
     [10,45,67]]

B = [[5,6,8],
     [7,7,7],
     [56,45,34]]

result =[[0,0,0],
         [0,0,0,],
         [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] +B[i][j]

for r in result:
     print(r)       