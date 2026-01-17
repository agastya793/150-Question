#  Write a program to generate a matrix where the elements alternate between 0 and 1.

rows = int(input("enter number of rows: "))
cols = int(input("enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = (i +j) % 2  # 0 if even ,1 if odd
        row.append(value)
    matrix.append(row)   
for r in matrix:
    print(*r)     