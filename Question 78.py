# Write a program to generate a matrix where each element at position (i, j) is the product of i and j.

'''rows = int(input("rows: "))
cols = int(input("cols: "))

matrix = [[i*j for j in range(cols) for i in range(rows)]]

for row in matrix:
    print(row)'''

    # another method 

def generate_product_matrix(rows,cols):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i*j)
        matrix.append(row)    
    return matrix

r = int(input("enter number of rows: "))   
c = int(input("enter number of columns: ")) 
result = generate_product_matrix(r,c)

print("generated matrix: ")
for row in result:
    print(row)

    