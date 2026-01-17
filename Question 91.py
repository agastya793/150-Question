# Write a program to generate Pascal’s Triangle up to N rows.

n = int(input("enter number of rows: "))
triangle = []
for i in range(n):
    row = [1] # first element is always 1
    if i> 0:
        for j in range(1,i):
            value = triangle[i-1][j-1] + triangle[i-1][j]

            row.append(value)
        row.append(1)    # last element is always 1
    triangle.append(row)    
                       
for row in triangle:
    print(*row)